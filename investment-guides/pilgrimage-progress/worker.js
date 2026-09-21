// The only server-side code on the senior guide. One route: a senior picks a
// session on the page and this tells Mike which one. Everything else falls
// through to the static asset it always was.
//
// It books nothing and charges nothing. HoneyBook has no write API a Worker
// could reach, and a page that told a family they were booked when no contract
// existed would be a lie with a deposit attached. The contract and the invoice
// are still built afterwards in HoneyBook; what this removes is the ambiguity
// about which session they meant.
//
// Same shape as the wedding quote pages (mikethezier-weddings/src/index.js).
// Deliberately not a framework.

const MAX = { tier: 40, label: 120, price: 24, name: 120, email: 200, phone: 40,
              school: 160, timing: 120, note: 2000 };

const FALLBACK_TO = "mike@pilgrimagemedia.com";

const json = (obj, status) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });

// Never trust the client's maxlength — it's a hint to the browser, not a
// constraint on the request. Single-line fields lose every control character:
// `name` is interpolated into the Subject header, where a stray CR or LF is a
// header-injection vector. The note keeps its newlines and loses the rest.
function clean(value, limit, multiline) {
  let s = String(value == null ? "" : value);
  s = multiline
    ? s.replace(/\r\n?/g, "\n").replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "")
    : s.replace(/[\x00-\x1F\x7F]+/g, " ").replace(/ {2,}/g, " ");
  return s.trim().slice(0, limit);
}

const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

// Good enough on purpose: the only real test of an address is whether mail to
// it is answered, and a stricter regex rejects valid addresses more often than
// it catches typos.
const looksLikeEmail = (s) => /^[^\s@]+@[^\s@.]+(\.[^\s@.]+)+$/.test(s);

function parse(form) {
  const f = (k) => clean(form.get(k), MAX[k] || 200);
  return {
    tier: f("tier"),       // mini | full | keepsake
    label: f("label"),     // its human name, so the email reads without a lookup
    price: f("price"),
    name: f("name"),
    email: f("email"),
    phone: f("phone"),
    school: f("school"),
    timing: f("timing"),
    note: clean(form.get("note"), MAX.note, true),
    honeypot: clean(form.get("website"), 200),
  };
}

function validate(i) {
  if (i.honeypot) return "spam";
  if (!i.tier) return "Something went wrong picking that session. Please email mike@pilgrimagemedia.com and he’ll sort it out.";
  if (!i.name) return "Please add your name so I know who I’m talking to.";
  if (!i.email) return "Please add an email address so I can write back.";
  if (!looksLikeEmail(i.email)) return "That email address doesn’t look right — mind checking it?";
  return null;
}

function compose(i, rateCard) {
  const rows = [
    ["Session", i.label || i.tier],
    ["Price", i.price],
    ["Rate card", rateCard],
    ["Name", i.name],
    ["Email", i.email],
    ["Phone", i.phone],
    ["School", i.school],
    ["Hoping to shoot", i.timing],
  ].filter(([, v]) => v);

  const text =
    rows.map(([k, v]) => `${k}: ${v}`).join("\n") +
    (i.note ? `\n\n---\n\n${i.note}\n` : "\n") +
    `\n---\nChosen from the Progress Sessions guide (${rateCard} rates).\n` +
    `Nothing is booked yet — the contract and invoice still need building in HoneyBook.\n`;

  const html =
    `<table style="font-family:system-ui,sans-serif;font-size:14px;border-collapse:collapse">` +
    rows
      .map(
        ([k, v]) =>
          `<tr><td style="padding:3px 14px 3px 0;color:#8C867C">${esc(k)}</td>` +
          `<td style="padding:3px 0"><strong>${esc(v)}</strong></td></tr>`
      )
      .join("") +
    `</table>` +
    (i.note
      ? `<hr style="border:0;border-top:1px solid #E4E1DA;margin:18px 0">` +
        `<div style="font-family:system-ui,sans-serif;font-size:15px;line-height:1.6;white-space:pre-wrap">${esc(i.note)}</div>`
      : "") +
    `<p style="font-family:system-ui,sans-serif;font-size:12px;color:#8C867C;margin-top:24px">` +
    `Chosen from the Progress Sessions guide (${esc(rateCard)} rates).<br>` +
    `Nothing is booked yet — the contract and invoice still need building in HoneyBook.</p>`;

  return { text, html };
}

async function deliver(env, { subject, text, html, replyTo }) {
  if (!env.RESEND_API_KEY) {
    // Distinguish "no binding" from "binding present but empty" — an empty
    // value is what a non-interactive `wrangler secret put` leaves behind and
    // looks identical to a missing secret from inside the Worker. Length only;
    // never log the key itself.
    throw new Error(
      `RESEND_API_KEY unusable (type ${typeof env.RESEND_API_KEY}, length ${String(env.RESEND_API_KEY ?? "").length})`
    );
  }
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: env.INQUIRY_FROM || "Progress Sessions <progress@pilgrimage.media>",
      to: [env.INQUIRY_TO || FALLBACK_TO],
      ...(replyTo ? { reply_to: replyTo } : {}),
      subject,
      text,
      html,
    }),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => "");
    throw new Error(`Resend returned ${res.status}: ${detail.slice(0, 300)}`);
  }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/api/choose") return env.ASSETS.fetch(request);
    if (request.method !== "POST") {
      return new Response("Method not allowed", { status: 405, headers: { allow: "POST" } });
    }

    const rateCard = env.RATE_CARD || "Regional";
    // A form posted by the browser navigates and expects a page back; the
    // page's own script asks for JSON so it can answer in place.
    const wantsJson = (request.headers.get("accept") || "").includes("application/json");
    const reply = (ok, message, status) =>
      wantsJson
        ? json({ ok, message }, status)
        : new Response(noticePage(ok ? "Thank you" : "That didn’t send", message), {
            status,
            headers: { "content-type": "text/html; charset=utf-8" },
          });

    let i;
    try {
      i = parse(await request.formData());
    } catch {
      return reply(false, "That didn’t come through in a format I could read.", 400);
    }

    const problem = validate(i);
    // A bot gets the same answer a person gets: telling it which check it
    // failed is free tuning advice. Nothing is sent.
    if (problem === "spam") return reply(true, "Thank you — Mike has been told.", 200);
    if (problem) return reply(false, problem, 400);

    try {
      const { text, html } = compose(i, rateCard);
      await deliver(env, {
        subject: `Progress Session chosen — ${i.name} — ${i.label || i.tier}`,
        text,
        html,
        // So hitting reply in Mail writes to the family, not to a sending
        // address with no mailbox behind it.
        replyTo: i.email,
      });
    } catch (err) {
      // This person has just made a decision about hiring Mike. Never answer
      // "thanks!" for something that was dropped on the floor.
      console.error("Choose send failed:", err && err.message,
        JSON.stringify({ tier: i.tier, email: i.email }));
      return reply(
        false,
        "Something went wrong sending that — sorry. Please email mike@pilgrimagemedia.com and he’ll pick it straight up.",
        502
      );
    }

    return reply(
      true,
      "Thank you — Mike has been told, and he’ll be in touch shortly with dates and your contract.",
      200
    );
  },
};

// The no-JS answer. The browser has navigated away from the guide, so this has
// to carry both the outcome and the way back.
function noticePage(heading, message) {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>${esc(heading)} — Mike Thezier Photography</title>
<style>
  body { margin:0; min-height:100vh; display:grid; place-items:center; padding:2rem;
         background:#fcfbf8; color:#262524; font:400 1rem/1.7 "Avenir Next","Helvetica Neue",Helvetica,Arial,sans-serif; }
  main { max-width:32rem; text-align:center }
  h1 { font-family:Georgia,serif; font-style:italic; font-weight:400; font-size:2rem; margin:0 0 1rem }
  a { color:#b3873f }
  @media (prefers-color-scheme: dark) { body { background:#191817; color:#ece5d9 } a { color:#c9a05c } }
</style></head>
<body><main>
  <h1>${esc(heading)}</h1>
  <p>${esc(message)}</p>
  <p><a href="/">Back to the guide</a></p>
</main></body></html>`;
}
