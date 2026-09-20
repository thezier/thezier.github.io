# -*- coding: utf-8 -*-
"""Design 8 — Rail.

A sticky rail down the left carries the wordmark, contact and the section
links; the wide right column does the reading. The link for whatever is on
screen lights up as you scroll, so the rail doubles as a position indicator.

The three sections alternate with photographs -- Family, frames, Locations,
frames, Legacy, frames -- rather than sitting in one block, because each idea
wants a picture under it.

Photographs run two and three up, so slots land at 540px and 350px, both
inside the native size of every image here. Nothing is enlarged.
"""
import content as C
from common import A, details_block, pick, page

CSS = """
  .shell { max-width: 80rem; margin: 0 auto; padding: 0 2rem; display: grid; gap: 0; }
  @media (min-width: 60rem) { .shell { grid-template-columns: 15rem 1fr; gap: 4rem; align-items: start; } }
  @media (max-width: 46rem) { .shell { padding: 0 1.25rem; } }

  /* ---------- Rail ---------- */
  .rail { padding: 1.5rem 0 1rem; }
  @media (min-width: 60rem) {
    .rail { position: sticky; top: 0; height: 100vh; display: flex; flex-direction: column;
            padding: 2.5rem 0; }
  }
  .rail .wm { width: 100%; max-width: 11rem; }
  .wm--dark { display: var(--wordmark-dark); } .wm--light { display: var(--wordmark-light); }
  .rail .eyebrow { font-size: .625rem; letter-spacing: .22em; text-transform: uppercase;
                   color: var(--ink-soft); margin-top: 1rem; line-height: 1.8; }

  .rail nav { margin-top: 1.75rem; display: flex; flex-direction: column; gap: .1rem; }
  .rail nav a { font-size: .6875rem; letter-spacing: .18em; text-transform: uppercase;
                color: var(--ink-soft); text-decoration: none; padding: .42rem 0 .42rem .85rem;
                border-left: 2px solid transparent; transition: color .18s ease, border-color .18s ease; }
  .rail nav a:hover { color: var(--ink); }
  .rail nav a.is-current { color: var(--gold); border-left-color: var(--gold); }
  @media (prefers-reduced-motion: reduce) { .rail nav a { transition: none; } }

  .rail .contact { margin-top: auto; padding-top: 1.75rem; font-size: .8125rem; line-height: 1.8; }
  .rail .contact a { color: var(--ink); text-decoration: none; display: block; }
  .rail .contact a:hover { color: var(--gold); }
  .rail .badge { width: 2.5rem; margin-bottom: .9rem; }
  .bd--dark { display: var(--wordmark-dark); } .bd--light { display: var(--wordmark-light); }

  /* On a phone the rail is a header, not a column: the nav scrolls sideways
     instead of stacking eleven lines of type above the page. */
  @media (max-width: 59.99rem) {
    .rail { border-bottom: 1px solid var(--gold); display: grid; gap: 1rem; }
    .rail .wm { max-width: 9.5rem; }
    .rail .eyebrow { margin-top: .5rem; }
    .rail nav { margin-top: 0; flex-direction: row; gap: .35rem; overflow-x: auto;
                -webkit-overflow-scrolling: touch; scrollbar-width: none;
                margin-inline: -1.25rem; padding-inline: 1.25rem; }
    .rail nav::-webkit-scrollbar { display: none; }
    .rail nav a { white-space: nowrap; border-left: 0; border-bottom: 2px solid transparent;
                  padding: .3rem 0 .5rem; }
    .rail nav a.is-current { border-left: 0; border-bottom-color: var(--gold); }
    .rail .contact { display: none; }
  }

  .main { padding: 2rem 0 4rem; }
  @media (min-width: 60rem) { .main { padding: 2.5rem 0 5rem; } }

  h1 { font-family: 'Marion', Didot, Georgia, serif; font-style: italic; font-weight: 400;
       font-size: clamp(2.4rem, 6.5vw, 4rem); line-height: 1.02; }
  .tagline { font-family: 'Marion', Didot, Georgia, serif; font-style: italic; color: var(--gold);
             font-size: clamp(1.45rem, 3vw, 2rem); line-height: 1.2; margin-top: 1rem;
             padding-bottom: 2rem; border-bottom: 1px solid var(--gold); }

  /* ---------- The three sections, alternating with frames ---------- */
  .creed { padding: 2.75rem 0 0; }
  .creed h2 { font-size: .6875rem; letter-spacing: .24em; text-transform: uppercase;
              color: var(--gold); margin-bottom: .85rem; }
  .creed p { font-size: 1.0625rem; line-height: 1.78; }
  .creed p + p { margin-top: .95rem; }

  /* Only two of these photographs are landscape. A portrait frame forced into
     a wide crop loses its subject, so a row is either all portrait at 3:4 or a
     single landscape shown at its own ratio -- never mixed. */
  .frames { display: grid; gap: 1rem; margin-top: 1.75rem; }
  .frames--2 { grid-template-columns: repeat(2, 1fr); }
  .frames--3 { grid-template-columns: repeat(3, 1fr); }
  @media (max-width: 40rem) { .frames--3 { grid-template-columns: repeat(2, 1fr); } }
  .frames img { width: 100%; aspect-ratio: 3/4; object-fit: cover; }
  .frames--full { grid-template-columns: 1fr; }
  .frames--full img { aspect-ratio: auto; object-fit: contain; }

  .block { padding: 3.25rem 0 0; }
  .kicker { font-size: .6875rem; letter-spacing: .24em; text-transform: uppercase;
            color: var(--gold); margin-bottom: 1rem; }
  h2.head { font-family: 'Marion', Didot, Georgia, serif; font-style: italic; font-weight: 400;
            font-size: clamp(1.8rem, 3vw, 2.35rem); line-height: 1.12; margin-bottom: 1rem; }
  .block p { line-height: 1.75; }
  .block p + p { margin-top: .9rem; }
  h3.beat { font-family: 'Marion', Didot, Georgia, serif; font-style: italic; font-size: 1.28rem;
            margin: 1.85rem 0 .6rem; }

  .two { display: grid; gap: 2rem 3rem; align-items: start; }
  @media (min-width: 52rem) {
    .two { grid-template-columns: .85fr 1.15fr; }
    /* Sits the copy below the kicker line rather than level with it, so the
       column reads as part of About me instead of a second column beside it. */
    .two > :last-child { padding-top: 4.5rem; }
  }

  .links { display: flex; flex-wrap: wrap; gap: .25rem 1.25rem; margin-top: 1.1rem; font-size: .9375rem; }
  .links a { color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--rule); }
  .links a:hover { color: var(--gold); border-color: var(--gold); }

  /* ---------- Packages: equal height, and the note spans the full set ------- */
  .tiers { display: grid; gap: 1.25rem; }
  @media (min-width: 52rem) { .tiers { grid-template-columns: repeat(3, 1fr); } }
  .tier { background: var(--panel); padding: 1.5rem 1.25rem 1.25rem;
          display: flex; flex-direction: column; height: 100%; }
  .tier--feature { outline: 1px solid var(--gold); outline-offset: -1px; }
  .tier .name { font-family: 'Marion', Didot, Georgia, serif; font-style: italic; font-size: 1.45rem; }
  .tier .hint { font-size: .72rem; color: var(--ink-soft); margin-top: .1rem; }
  .tier .price { font-family: 'Marion', Didot, Georgia, serif; font-size: 2.1rem; color: var(--gold);
                 margin: .6rem 0 .75rem; line-height: 1; font-variant-numeric: tabular-nums; }
  .tier .builtfor { font-size: .9rem; line-height: 1.5; padding-bottom: .85rem;
                    border-bottom: 1px solid var(--panel-line); }
  .tier ul { margin-top: .85rem; }
  .tier li { font-size: .875rem; padding-left: 1rem; position: relative; margin-top: .38rem; line-height: 1.45; }
  .tier li::before { content: "\\2014"; position: absolute; left: 0; color: var(--gold); }
  .tier .why { font-size: .8125rem; color: var(--ink-soft); margin-top: .85rem; line-height: 1.5; }
  .tier .why strong { color: var(--ink); font-weight: 400; }
  /* Pushes the button to the bottom of whichever card is tallest. */
  .tier .pick { margin-top: auto; padding-top: 1.05rem; }

  .fine { font-size: .8125rem; font-style: italic; color: var(--ink-soft); line-height: 1.6;
          margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid var(--rule); }

  .faq { display: grid; gap: 1.4rem 3rem; }
  @media (min-width: 52rem) { .faq { grid-template-columns: 1fr 1fr; } }
  .faq dt { font-family: 'Marion', Didot, Georgia, serif; font-style: italic; font-size: 1.05rem; }
  .faq dd { margin-top: .3rem; font-size: .9rem; color: var(--ink-soft); line-height: 1.65; }
"""

# Highlights the rail link for whatever is on screen. Progressive: with the
# script blocked the links are still anchors and the page still reads.
SPY = """
<script>
(function () {
  "use strict";
  var links = [].slice.call(document.querySelectorAll('.rail nav a[href^="#"]'));
  if (!links.length || !window.IntersectionObserver) return;

  var byId = {};
  var targets = [];
  links.forEach(function (a) {
    var el = document.getElementById(a.getAttribute("href").slice(1));
    if (el) { byId[el.id] = a; targets.push(el); }
  });
  if (!targets.length) return;

  var reduceMotion = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var visible = {};
  function paint() {
    // The section nearest the top of those on screen wins, so scrolling past a
    // short section does not leave two links lit or none.
    var best = null, bestTop = Infinity;
    targets.forEach(function (el) {
      if (!visible[el.id]) return;
      var top = el.getBoundingClientRect().top;
      if (top < bestTop) { bestTop = top; best = el.id; }
    });
    links.forEach(function (a) { a.classList.remove("is-current"); });
    if (!best || !byId[best]) return;
    var a = byId[best];
    a.classList.add("is-current");

    // On a phone the rail is a horizontal strip, so the link that just lit up
    // can easily be off to one side. Bring it back into the strip -- but only
    // scroll the strip itself, never the page.
    var nav = a.parentNode;
    if (nav.scrollWidth <= nav.clientWidth + 1) return;
    var left = a.offsetLeft - (nav.clientWidth - a.offsetWidth) / 2;
    if (typeof nav.scrollTo === "function") {
      nav.scrollTo({ left: left, behavior: reduceMotion ? "auto" : "smooth" });
    } else {
      nav.scrollLeft = left;
    }
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
    paint();
  }, { rootMargin: "-20% 0px -60% 0px", threshold: 0 });

  targets.forEach(function (el) { io.observe(el); });
})();
</script>
"""

def frames(items, cls="frames--3"):
    return ('<div class="frames %s">%s</div>' % (cls, "".join(
        '<img src="%s" alt="%s" width="%s" height="%s" loading="lazy">'
        % (i["src"], i["alt"], i["w"], i["h"]) for i in items)))

def build():
    g = A["gallery"]
    hero_a = {"src": A["hero_a"], "alt": "A couple standing forehead to forehead in a eucalyptus grove, their two children running circles around them",
              "w": A["hero_a_wh"][0], "h": A["hero_a_wh"][1]}
    hero_b = {"src": A["hero_b"], "alt": "A mother sitting on the bed at home holding her newborn, her toddler leaning over her shoulder",
              "w": A["hero_b_wh"][0], "h": A["hero_b_wh"][1]}
    hero_c = {"src": A["hero_c"], "alt": "Parents forehead to forehead outdoors with their three children gathered around them",
              "w": A["hero_c_wh"][0], "h": A["hero_c_wh"][1]}

    # Each idea gets its own frames underneath it. Portraits stay in portrait
    # rows; the two landscape frames get a full-width row of their own at their
    # native ratio, which is where they actually look like something.
    sets = [
        frames([hero_a, hero_c, g[0]], "frames--3"),
        frames([hero_b, g[1], g[6]], "frames--3"),
        frames([g[2], g[3], g[4]], "frames--3"),
    ]
    ids = ["family", "locations", "legacy"]

    creed = "\n".join(
        '    <section class="creed" id="%s">\n      <h2>%s</h2>\n%s\n      %s\n    </section>'
        % (i, h, "\n".join("      <p>%s</p>" % para for para in p.split("\n\n")), f)
        for (h, p), i, f in zip(C.SECTIONS, ids, sets))

    beats = "\n".join('      <h3 class="beat">%s</h3>\n%s'
                      % (h, "\n".join("      <p>%s</p>" % x for x in ps)) for h, ps in C.BEATS)
    tiers = []
    for t in C.TIERS:
        why = ('<p class="why"><strong>%s</strong> %s</p>' % t["why"]) if t["why"] else ""
        tiers.append("""          <div class="tier%s">
            <p class="name">%s</p><p class="hint">%s</p>
            <p class="price">$%s</p>
            <p class="builtfor">%s</p>
            <ul>%s</ul>
            %s
            %s
          </div>""" % (" tier--feature" if t["feature"] else "", t["name"], t["hint"], t["price"],
                       t["builtfor"], "".join("<li>%s</li>" % i for i in t["includes"]), why, pick(t)))
    faq = "\n".join('        <div><dt>%s</dt><dd>%s</dd></div>' % qa for qa in C.FAQ)

    body = """<div class="shell">
  <aside class="rail">
    <div>
      <img class="wm wm--dark" src="%(wmd)s" alt="Mike Thezier Photography" width="1000" height="208">
      <img class="wm wm--light" src="%(wml)s" alt="" aria-hidden="true" width="1000" height="208">
      <p class="eyebrow">Family Sessions<br>Southern California</p>
    </div>
    <nav aria-label="Sections">
      <a href="#connection">Connection</a>
      <a href="#about">About</a>
      <a href="#experience">The experience</a>
      <a href="#sessions">Sessions &amp; pricing</a>
      <a href="#questions">Questions</a>
      <a href="#next">Next step</a>
    </nav>
    <div class="contact">
      <img class="badge bd--dark" src="%(bdd)s" alt="" aria-hidden="true" width="500" height="500">
      <img class="badge bd--light" src="%(bdl)s" alt="" aria-hidden="true" width="500" height="500">
      <a href="tel:+19515871238">951.587.1238</a>
      <a href="mailto:mike@mikethezier.com">mike@mikethezier.com</a>
      <a href="https://mikethezier.com">mikethezier.com</a>
    </div>
  </aside>

  <main class="main">
    <h1>%(title)s</h1>
    <p class="tagline">%(tagline)s</p>

    <div id="connection">
%(creed)s
    </div>

    <section class="block two" id="about">
      <div>
        <p class="kicker">About me</p>
        <img src="%(portrait)s" alt="Mike Thezier outdoors with his camera" width="%(pw)s" height="%(ph)s" loading="lazy">
      </div>
      <div>
        <h2 class="head">It&rsquo;s my goal to make photographs that tell your story.</h2>
        <p>%(about1)s</p>
        <p>%(about2)s</p>
        <div class="links">
          <a href="tel:+19515871238">951.587.1238</a>
          <a href="mailto:mike@mikethezier.com">mike@mikethezier.com</a>
          <a href="https://mikethezier.com">mikethezier.com</a>
        </div>
      </div>
    </section>

    <section class="block" id="experience">
      <p class="kicker">The experience</p>
%(beats)s
      %(expframes)s
    </section>

    <section class="block" id="sessions">
      <p class="kicker">Sessions &amp; pricing</p>
      <form class="choose" method="post" action="/api/choose">
        <div class="tiers">
%(tiers)s
        </div>
        <p class="fine">%(fine)s</p>
        <div class="details" id="details" style="margin-top:2.75rem;max-width:44rem">
          <h2 class="head" style="font-size:1.45rem">Your details</h2>
%(details)s
        </div>
      </form>
    </section>

    <section class="block" id="questions">
      <p class="kicker">Questions</p>
      <dl class="faq">
%(faq)s
      </dl>
    </section>

    <section class="block" id="next">
      <p class="kicker">Next step</p>
      <p>%(next1)s</p>
      <p>%(next2)s</p>
    </section>
  </main>
</div>
%(spy)s""" % {
      "wmd": A["wordmark_dark"], "wml": A["wordmark_light"],
      "bdd": A["badge_dark"], "bdl": A["badge_light"],
      "title": C.TITLE, "tagline": C.TAGLINE, "creed": creed,
      "portrait": A["portrait"], "pw": A["portrait_wh"][0], "ph": A["portrait_wh"][1],
      "about1": C.ABOUT[0], "about2": C.ABOUT[1], "beats": beats,
      "expframes": frames([g[7]], "frames--full"),
      "tiers": "\n".join(tiers), "details": details_block(), "fine": C.FINENOTE, "faq": faq,
      "next1": C.NEXT[0], "next2": C.NEXT[1], "spy": SPY,
    }
    return page("rail", "Rail", CSS, body)
