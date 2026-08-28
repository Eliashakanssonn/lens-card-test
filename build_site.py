#!/usr/bin/env python3
"""Standalone showcase page: one layout, a Control/Variant switch that flips
every card image at once. Same measured theme tokens as the canvas artboards."""
import pathlib
OUT = pathlib.Path(__file__).parent

BG, INK, BLACK, PINK, TINT = "#fbfbfb", "#1d1d1d", "#000000", "#fc3b62", "#efefef"

P = [
    dict(k="jade",       shade="Jade Green",         badges=["SAVE 20%"]),
    dict(k="aquamarine", shade="Aquamarine Blue",    badges=["SAVE 20%", "BESTSELLER"]),
    dict(k="graphite",   shade="Graphite Dark Grey", badges=["SAVE 20%"]),
    dict(k="honey",      shade="Honey Hazel Brown",  badges=["SAVE 20%"]),
]

def card(p):
    badges = "".join(
        '<span class="badge %s">%s</span>' % ("b-best" if b == "BESTSELLER" else "b-save", b)
        for b in p["badges"])
    return f"""        <article class="card">
          <div class="media">
            <img class="ctrl" src="img/{p['k']}_ctrl.jpg" alt="{p['shade']} packaging" loading="lazy">
            <img class="still" src="img/{p['k']}_still.png" alt="{p['shade']} on the eye" loading="lazy">
            <img class="anim" data-gif="img/{p['k']}_hover.gif" alt="" loading="lazy">
            <div class="badges">{badges}</div>
          </div>
          <div class="meta">
            <div class="names">
              <span class="p-title">{p['shade']}</span>
              <span class="p-dur">For 1-Month Use</span>
            </div>
            <div class="prices">
              <span class="p-now">343 kr /</span>
              <span class="p-was">429 kr</span>
            </div>
          </div>
          <a class="cta" href="#" onclick="return false">SHOP NOW</a>
        </article>"""

CARDS = "\n".join(card(p) for p in P)

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<title>Product card test &mdash; close-up on the eye</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&display=swap">
<style>
  *, *::before, *::after {{ box-sizing: border-box; }}
  body {{ margin: 0; background: {BG}; color: {INK};
         font-family: 'Jost','Gordita','Helvetica Neue',Arial,sans-serif;
         -webkit-font-smoothing: antialiased; }}
  .wrap {{ max-width: 1320px; margin: 0 auto; padding: 0 40px 96px; }}
  .wrap.head {{ padding-bottom: 0; }}

  header {{ padding: 72px 0 0; }}
  h1 {{ font-size: 34px; font-weight: 500; letter-spacing: -.01em; margin: 0 0 10px; color: {BLACK}; }}
  .lede {{ font-size: 16px; line-height: 1.65; color: #6a6a6a; margin: 0; max-width: 660px; }}

  .bar {{ position: sticky; top: 0; z-index: 20; background: rgba(251,251,251,.92);
          backdrop-filter: blur(10px); border-bottom: 1px solid #e8e8e8; margin-top: 36px; }}
  .bar-in {{ max-width: 1320px; margin: 0 auto; padding: 16px 40px;
             display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }}
  .switch {{ display: inline-flex; background: #ededed; border-radius: 999px; padding: 4px; gap: 4px; }}
  .switch button {{ font: inherit; font-size: 14px; font-weight: 600; letter-spacing: .04em;
                    text-transform: uppercase; border: 0; cursor: pointer; padding: 9px 22px;
                    border-radius: 999px; background: transparent; color: #7a7a7a;
                    transition: background .16s ease, color .16s ease; }}
  .switch button[aria-pressed="true"] {{ background: {INK}; color: #fff; }}
  .hint {{ font-size: 14px; color: #8a8a8a; }}
  .hint b {{ color: {INK}; font-weight: 600; }}

  section {{ padding-top: 64px; }}
  .sec-head {{ display: flex; align-items: baseline; gap: 14px; margin-bottom: 28px; }}
  .sec-head h2 {{ font-size: 13px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase;
                  color: #9a9a9a; margin: 0; }}
  .sec-head span {{ font-size: 14px; color: #b4b4b4; }}
  .store-h2 {{ font-family: Georgia,'Times New Roman',serif; font-size: 38px; font-weight: 400;
               margin: 0 0 34px; color: {BLACK}; }}

  .filters {{ display: flex; justify-content: space-between; align-items: center;
              padding-bottom: 18px; border-bottom: 1px solid #e6e6e6; margin-bottom: 34px; }}
  .filters div {{ display: flex; gap: 30px; }}
  .filters span {{ font-size: 15px; }}
  .filters .count {{ font-size: 14px; color: #9a9a9a; }}

  .grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 28px; }}

  .card {{ display: flex; flex-direction: column; gap: 12px; }}
  .media {{ position: relative; border-radius: 5px; overflow: hidden; aspect-ratio: 4 / 5; background: {TINT}; }}
  .media img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
  .media .still, .media .anim {{ position: absolute; inset: 0; }}
  .media .anim {{ opacity: 0; transition: opacity .18s ease; }}
  /* control is the default; variant swaps which layer is visible */
  .media .still {{ opacity: 0; }}
  body.variant .media .ctrl {{ opacity: 0; }}
  body.variant .media .still {{ opacity: 1; }}
  body.variant .card:hover .media .anim {{ opacity: 1; }}
  .media .ctrl {{ transition: opacity .18s ease; }}
  .media .still {{ transition: opacity .18s ease; }}

  .badges {{ position: absolute; top: 12px; left: 12px; display: flex; flex-wrap: wrap; gap: 6px;
             max-width: calc(100% - 24px); }}
  .badge {{ font-size: 12px; font-weight: 700; padding: 5px 11px; border-radius: 14px;
            letter-spacing: .02em; line-height: 1.1; }}
  .b-save {{ background: {PINK}; color: {BG}; }}
  .b-best {{ background: {INK}; color: #fff; }}

  .meta {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; }}
  .names {{ display: flex; flex-direction: column; gap: 2px; }}
  .p-title {{ font-size: 16px; font-weight: 500; color: {BLACK}; line-height: 1.3; min-height: 2.6em; }}
  .p-dur {{ font-size: 14px; font-weight: 400; }}
  .prices {{ display: flex; flex-direction: column; align-items: flex-end; gap: 2px; white-space: nowrap; }}
  .p-now {{ font-size: 15px; font-weight: 500; color: {PINK}; }}
  .p-was {{ font-size: 15px; font-weight: 500; text-decoration: line-through; }}
  .cta {{ display: block; margin-top: auto; text-align: center; background: {INK}; color: #fff;
          font-size: 15px; font-weight: 500; padding: 14px 0; border-radius: 5px; text-decoration: none; }}

  .phone {{ width: 390px; max-width: 100%; border: 1px solid #e4e4e4; border-radius: 22px;
            padding: 18px; background: #fff; }}
  .phone .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }}
  .phone .badge {{ font-size: 10px; padding: 4px 8px; border-radius: 12px; }}
  .phones {{ display: flex; gap: 40px; flex-wrap: wrap; }}

  .note {{ margin-top: 26px; font-size: 14px; line-height: 1.7; color: #7a7a7a; max-width: 700px; }}

  @media (max-width: 1080px) {{ .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
  @media (max-width: 720px)  {{ .wrap, .bar-in {{ padding-left: 20px; padding-right: 20px; }}
                                .store-h2 {{ font-size: 28px; }} h1 {{ font-size: 26px; }} }}
</style>
</head>
<body class="control">

<div class="wrap head">
  <header>
    <h1>Product card test &mdash; close-up on the eye</h1>
    <p class="lede">Today the card leads with the box. This swaps it for the close-up already
      sitting on the product page &mdash; the shot that answers &ldquo;what will these look like
      on me?&rdquo; before anyone clicks.</p>
  </header>
</div>

<div class="bar">
  <div class="bar-in">
    <div class="switch" role="group" aria-label="Which version to show">
      <button id="b-control" aria-pressed="true">Control</button>
      <button id="b-variant" aria-pressed="false">Variant</button>
    </div>
    <span class="hint" id="hint">Showing the cards as they are today.</span>
  </div>
</div>

<div class="wrap">
  <section>
    <div class="sec-head"><h2>Homepage</h2><span>bestseller row</span></div>
    <h2 class="store-h2">Our bestsellers.</h2>
    <div class="grid">
{CARDS}
    </div>
  </section>

  <section>
    <div class="sec-head"><h2>Collection</h2><span>coloured lenses</span></div>
    <div class="filters">
      <div><span>Price</span><span>Colour</span><span>Duration</span><span>Recommended for Eyes</span></div>
      <span class="count">36 items</span>
    </div>
    <div class="grid">
{CARDS}
    </div>
  </section>

  <section>
    <div class="sec-head"><h2>Mobile</h2><span>390px, two up</span></div>
    <div class="phones">
      <div class="phone">
        <div class="grid">
{card(P[0])}
{card(P[1])}
        </div>
      </div>
    </div>
    <p class="note">Hover does not exist on a phone, so mobile gets the still only &mdash;
      the still has to carry the test on its own.</p>
  </section>
</div>

<script>
  var body = document.body, hint = document.getElementById('hint');
  var bC = document.getElementById('b-control'), bV = document.getElementById('b-variant');

  // GIFs are only fetched once the variant is first shown, so the page opens fast
  var gifsLoaded = false;
  function loadGifs() {{
    if (gifsLoaded) return; gifsLoaded = true;
    document.querySelectorAll('.anim[data-gif]').forEach(function (img) {{
      // eager, not lazy: a deferred clip means the first hover plays nothing
      img.loading = 'eager';
      img.src = img.getAttribute('data-gif');
    }});
  }}

  function show(variant) {{
    body.classList.toggle('variant', variant);
    body.classList.toggle('control', !variant);
    bV.setAttribute('aria-pressed', String(variant));
    bC.setAttribute('aria-pressed', String(!variant));
    hint.innerHTML = variant
      ? 'Hover a card &mdash; the clip plays. <b>That is the whole change.</b>'
      : 'Showing the cards as they are today.';
    if (variant) loadGifs();
  }}
  bC.addEventListener('click', function () {{ show(false); }});
  bV.addEventListener('click', function () {{ show(true); }});

  // left/right arrows flip it too
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'ArrowRight') show(true);
    if (e.key === 'ArrowLeft') show(false);
  }});
</script>
</body>
</html>
"""

(OUT / "index.html").write_text(HTML, encoding="utf-8")
print(f"index.html  {len(HTML):,} chars")
