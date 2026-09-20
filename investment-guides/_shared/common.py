# -*- coding: utf-8 -*-
"""Pieces every design needs, in the shape each design then styles."""
import json, pathlib


def load_assets(build_dir):
    return json.loads((pathlib.Path(build_dir) / "assets.json").read_text())

RESET = """
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--ground); color: var(--ink);
         font-family: 'CorporativeSans','Avenir Next',-apple-system,sans-serif;
         font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased; }
  img { max-width: 100%; height: auto; display: block; }
  h1,h2,h3,h4,p,dl,dd,ul { margin: 0; }
  ul { padding: 0; list-style: none; }

  /* --- the choose-a-session form: identical behaviour in all three --- */
  .pick { display: block; cursor: pointer; }
  .pick input { position: absolute; width: 1px; height: 1px; opacity: 0; pointer-events: none; }
  .pick-face { display: block; padding: .8rem 1rem; border: 1px solid var(--gold); color: var(--gold);
               text-align: center; font-size: .6875rem; letter-spacing: .2em; text-transform: uppercase;
               transition: background-color .15s ease, color .15s ease; }
  .pick:hover .pick-face { background: var(--gold); color: var(--ground); }
  .pick input:focus-visible + .pick-face { outline: 2px solid var(--gold); outline-offset: 2px; }
  .pick input:checked + .pick-face { background: var(--gold); color: var(--ground); }
  .pick input:checked + .pick-face::after { content: " \\2014 chosen"; }
  @media (prefers-reduced-motion: reduce) { .pick-face { transition: none; } }

  .chosen { background: var(--panel); border-left: 3px solid var(--gold); padding: .85rem 1rem;
            margin-bottom: 1.25rem; font-size: .9375rem; }
  .chosen b { font-weight: 400; color: var(--gold); }
  .fields { display: grid; gap: .9rem; margin-top: 1rem; }
  .fields label { display: flex; flex-direction: column; gap: .3rem; }
  .fields span { font-size: .6875rem; letter-spacing: .18em; text-transform: uppercase; color: var(--ink-soft); }
  .fields em { font-style: normal; text-transform: none; letter-spacing: .02em; opacity: .75; }
  .fields input, .fields textarea { font: inherit; font-size: .9375rem; color: var(--ink);
    background: var(--ground); border: 1px solid var(--rule); border-radius: 0; padding: .6rem .7rem;
    width: 100%; -webkit-appearance: none; }
  .fields textarea { resize: vertical; min-height: 4.5rem; }
  .fields input:focus-visible, .fields textarea:focus-visible { outline: 2px solid var(--gold);
    outline-offset: 1px; border-color: var(--gold); }
  .hp { position: absolute; left: -9999px; width: 1px; height: 1px; overflow: hidden; }
  .send { font: inherit; font-size: .6875rem; letter-spacing: .2em; text-transform: uppercase;
          margin-top: 1.25rem; width: 100%; padding: .95rem 1rem; background: var(--gold);
          color: var(--ground); border: 1px solid var(--gold); cursor: pointer; }
  .send[disabled] { opacity: .55; cursor: default; }
  .sendnote { font-size: .8125rem; font-style: italic; color: var(--ink-soft); margin-top: .85rem; }
  .formnote { margin-top: .85rem; padding: .8rem .9rem; background: var(--panel);
              border-left: 3px solid var(--gold); font-size: .9375rem; }
  .formnote.is-error { border-left-color: #b4483c; }
  @media (min-width: 37.5rem) {
    .fields { grid-template-columns: 1fr 1fr; }
    .fields .wide { grid-column: 1 / -1; }
    .send { width: auto; padding-inline: 2.5rem; }
  }
"""

def details_block(C):
    rows = []
    for nm, label, opt, req, ac in C.FIELDS:
        cls = ""
        auto = ' autocomplete="%s"' % ac if ac else ""
        t = ' type="email"' if nm == "email" else (' type="tel"' if nm == "phone" else "")
        r = " required" if req else ""
        em = ' <em>%s</em>' % opt if opt else ""
        ph = ' placeholder="%s"' % C.PLACEHOLDERS[nm] if nm in C.PLACEHOLDERS else ""
        rows.append('<label%s><span>%s%s</span><input name="%s"%s%s%s%s></label>' % (cls, label, em, nm, t, auto, ph, r))
    rows.append('<label class="wide"><span>Anything else <em>optional</em></span>'
                '<textarea name="note" rows="3"></textarea></label>')
    return """      <p class="chosen" hidden></p>
      <div class="fields">
        %s
      </div>
      <p class="hp" aria-hidden="true"><label>Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label></p>
      <input type="hidden" name="label" value="">
      <input type="hidden" name="price" value="">
      <button class="send" type="submit">Send to Mike</button>
      <p class="sendnote">Nothing is booked or charged here. I&rsquo;ll come back with dates, then
        send your contract and invoice through HoneyBook.</p>
      <p class="formnote" role="status" hidden></p>""" % "\n        ".join(rows)

def pick(t):
    return ('<label class="pick"><input type="radio" name="tier" value="%s" data-label="%s" '
            'data-price="$%s" required><span class="pick-face">Choose this one</span></label>'
            % (t["id"], t["name"], t["price"]))

def page(A, title, description, css, body, host):
    """sync-local.py rewrites `host` for the local card, so the canonical here
    names the regional one."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s &mdash; Mike Thezier Photography</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#fcfbf8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#191817" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s &mdash; Mike Thezier Photography">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="https://%(host)s/">
<link rel="canonical" href="https://%(host)s/">
<meta name="robots" content="noindex, nofollow">
</head>
<body>
<style>%(fonts)s
%(tokens)s
%(reset)s
%(css)s</style>
%(body)s
%(script)s
</body>
</html>
""" % {"title": title, "desc": description, "host": host, "fonts": A["fonts"], "tokens": A["tokens"],
       "reset": RESET, "css": css, "body": body, "script": A["script"]}
