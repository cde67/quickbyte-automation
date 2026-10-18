"""
Builds the QuickByte landing page (quickbyteshorts.pages.dev) - the link in the
Instagram bio and on the YouTube channel (Shorts descriptions and comments
aren't clickable, so this page is where every product link lives).

It's laid out like a small curated shop: in gift season (mid-October through
Christmas) the gift picks lead, grouped by budget; the rest of the gear
follows, then the latest live videos. Each product card uses:
  - picks.json for the name, a one-line reason and a rough price,
  - a still from our own video footage (never AI art or Amazon images),
  - a "Watch the video" link once that video is live.
Unposted scripts are never listed as videos.
"""
import datetime
import html
import json
import os
import re
import subprocess
import urllib.parse

import scripts as s

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")
IMG_DIR = os.path.join(DOCS_DIR, "img")

SITE_NAME = "QuickByte"
SITE_TAGLINE = "Short videos on which tech is worth buying, and which isn't"
SITE_URL = "https://quickbyteshorts.pages.dev"
SOCIALS = [("YouTube", "https://www.youtube.com/@quickbytetips"),
           ("TikTok", "https://www.tiktok.com/@quickbytetips"),
           ("Instagram", "https://www.instagram.com/quickbytetips")]
BUDGETS = [(25, "Under $25"), (50, "Under $50"), (100, "Under $100"), (999, "Worth the splurge")]


def load_env():
    env = {}
    path = os.path.join(SCRIPT_DIR, ".env")
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    env[k] = v
    return env


def _load_json(name, default):
    path = os.path.join(SCRIPT_DIR, name)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


PRODUCT_LINKS = _load_json("product_links.json", {})


def amazon_url(item, tag, search=None):
    """Direct product-page link when we've resolved a real ASIN for this
    item (see product_links.json) - falls back to a search link only for
    items not yet resolved."""
    link = PRODUCT_LINKS.get(item)
    if link:
        return f"{link['url']}?tag={tag}"
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(search or item)}&tag={tag}"


def _product_label(name):
    # "30W USB-C PD GaN charger" -> "30W USB-C PD GaN Charger" (keep acronyms as written)
    return " ".join(w if any(c.isupper() or c.isdigit() for c in w) else w.capitalize() for w in name.split())


def gift_season(today):
    return datetime.date(today.year, 10, 15) <= today <= datetime.date(today.year, 12, 26)


# ---------- product stills from our own footage ----------

def _clip_for(slug):
    """Path of a cached stock clip this video used: the shots recorded in its
    qa.json first (matched by Pexels id), then any cached clip for one of the
    script's footage queries (older renders didn't record their shots)."""
    manifest = _load_json(os.path.join("footage_cache", "manifest.json"), {})
    cached = [m for m in manifest.values() if os.path.exists(m.get("path", ""))]
    try:
        with open(os.path.join(SCRIPT_DIR, "videos", f"{slug}.qa.json")) as f:
            footage = json.load(f).get("footage", [])
    except (OSError, ValueError):
        footage = []
    for shot in footage:
        pid = shot.get("pexels_id")
        if shot.get("kind") != "clip" or not pid:
            continue
        for m in cached:
            if f"/{pid}/" in m.get("source_url", "") or m.get("pexels_page", "").rstrip("/").endswith(f"-{pid}"):
                return m["path"]
    entry = next((e for e in s.SCRIPTS if e["slug"] == slug), {})
    for q in entry.get("footage_queries", []):
        for m in cached:
            if m.get("query") == q:
                return m["path"]
    return None


def product_image(key, slugs, photo=None):
    """docs/img/<key>.jpg at 800x600: the hand-picked photo from picks.json
    when there is one, else a still from one of this product's videos.
    Returns the site-relative path, or None if neither is available."""
    fname = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-") + ".jpg"
    out = os.path.join(IMG_DIR, fname)
    if os.path.exists(out):
        return f"img/{fname}"
    if photo:
        os.makedirs(IMG_DIR, exist_ok=True)
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", photo, "-frames:v", "1",
                            "-vf", "scale=800:600:force_original_aspect_ratio=increase,crop=800:600",
                            "-q:v", "4", out], capture_output=True)
        if r.returncode == 0 and os.path.exists(out):
            return f"img/{fname}"
    for slug in slugs:
        clip = _clip_for(slug)
        if not clip:
            continue
        os.makedirs(IMG_DIR, exist_ok=True)
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.2", "-i", clip, "-frames:v", "1",
                            "-vf", "scale=800:600:force_original_aspect_ratio=increase,crop=800:600", "-q:v", "4", out],
                           capture_output=True)
        if r.returncode == 0 and os.path.exists(out):
            return f"img/{fname}"
    return None


# ---------- page ----------

STYLE = """
:root{--bg:#fbfaf8;--card:#fff;--ink:#14161a;--ink2:#3d424c;--muted:#6b707a;--line:#e9e6e1;
--accent:#ff6b4a;--accent-ink:#d9482a;--chip:#f2efea}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:inherit}
.wrap{max-width:980px;margin:0 auto;padding:36px 20px 72px}
.head{display:flex;align-items:center;gap:14px}
.head img{width:56px;height:56px;border-radius:50%}
.brand{font-weight:800;font-size:1.5rem;letter-spacing:-.02em;line-height:1.1}
.tagline{color:var(--muted);font-size:.95rem}
.socials{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 0}
.socials a{text-decoration:none;font-size:.85rem;font-weight:600;padding:7px 14px;border-radius:999px;background:var(--chip)}
.socials a:hover{background:var(--line)}
.season{margin:40px 0 6px;font-size:1.75rem;font-weight:800;letter-spacing:-.02em;line-height:1.2}
.season-sub{color:var(--ink2);max-width:620px;margin:0 0 6px}
.jump{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 6px}
.jump a{text-decoration:none;font-size:.85rem;font-weight:600;padding:6px 13px;border-radius:999px;border:1px solid var(--line);background:var(--card)}
.jump a:hover{border-color:var(--ink)}
h2{font-size:1.05rem;font-weight:800;margin:36px 0 14px;letter-spacing:-.01em}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.pick{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
.pick .ph{aspect-ratio:4/3;background:var(--chip);overflow:hidden}
.pick .ph img{width:100%;height:100%;object-fit:cover;display:block}
.pick .body{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.pick .name{font-weight:700;font-size:1.02rem;line-height:1.3}
.pick .price{color:var(--muted);font-size:.85rem}
.pick .note{color:var(--ink2);font-size:.92rem;flex:1}
.pick .row{display:flex;align-items:center;gap:12px;margin-top:8px;flex-wrap:wrap}
.buy{display:inline-block;text-decoration:none;background:var(--ink);color:#fff;font-weight:700;font-size:.88rem;padding:9px 16px;border-radius:999px}
.buy:hover{background:var(--accent-ink)}
.watch{font-size:.85rem;color:var(--muted);text-decoration:underline;text-underline-offset:3px}
.fine{color:var(--muted);font-size:.82rem;margin:22px 0 0;max-width:640px}
.vids{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}
.vids li{border-bottom:1px solid var(--line)}
.vids a{display:flex;justify-content:space-between;gap:16px;padding:13px 2px;text-decoration:none}
.vids a span:last-child{color:var(--muted);font-size:.85rem;white-space:nowrap}
.vids a:hover span:first-child{text-decoration:underline;text-underline-offset:3px}
footer{color:var(--muted);font-size:.82rem;text-align:center;padding:24px}
@media (max-width:520px){.season{font-size:1.45rem}.wrap{padding-top:26px}}
"""


def _card(p, tag):
    img = (f'<div class="ph"><img src="{p["img"]}" alt="" loading="lazy" width="800" height="600"></div>'
           if p["img"] else "")
    watch = (f'<a class="watch" href="{p["video"]}" target="_blank" rel="noopener">Watch the video</a>'
             if p["video"] else "")
    return f"""<article class="pick">{img}<div class="body">
<div class="name">{html.escape(p['name'])}</div>
<div class="price">{html.escape(p['price'])}</div>
<p class="note" style="margin:0">{html.escape(p['note'])}</p>
<div class="row"><a class="buy" href="{html.escape(p['url'])}" target="_blank" rel="noopener sponsored nofollow">See it on Amazon</a>{watch}</div>
</div></article>"""


def build_page(today=None):
    """Built for the person who just tapped "link in bio": gift picks first in
    season, then the rest of the gear, then the live videos (newest first)."""
    today = today or datetime.date.today()
    env = load_env()
    tag = env.get("AMAZON_ASSOCIATE_TAG", "").strip() or "PLACEHOLDER-20"
    meta = _load_json("picks.json", {})
    posted = _load_json("posted_log.json", {}).get("posted_slugs", [])
    videos = _load_json("performance_log.json", {}).get("videos", {})
    by_slug = {e["slug"]: e for e in s.SCRIPTS}
    live = [by_slug[slug] for slug in reversed(posted) if slug in by_slug]  # newest first

    # one card per product, wherever it appears in the library (live videos first)
    picks, seen = [], set()
    ordered = live + [e for e in s.SCRIPTS if e["slug"] not in set(posted)]
    for entry in ordered:
        aff = entry.get("affiliate")
        if not aff or aff["product_name"] in seen:
            continue
        key = aff["product_name"]
        seen.add(key)
        m = meta.get(key, {})
        slugs = [e["slug"] for e in ordered if (e.get("affiliate") or {}).get("product_name") == key]
        live_slug = next((x for x in slugs if x in posted), None)
        vid = videos.get(live_slug, {}).get("video_id") if live_slug else None
        picks.append({
            "key": key, "name": m.get("name") or _product_label(key), "note": m.get("note", ""),
            "price": m.get("price", ""), "budget": m.get("budget", 999), "gift": m.get("gift", False),
            "url": amazon_url(key, tag, aff.get("search_term")), "img": product_image(key, slugs, m.get("photo")),
            "video": f"https://www.youtube.com/shorts/{vid}" if vid else None, "live": bool(live_slug),
        })
    # live videos' picks first within each section, then by price
    picks.sort(key=lambda p: (not p["live"], p["budget"]))

    parts = []
    in_season = gift_season(today)
    gifts = [p for p in picks if p["gift"]] if in_season else []
    if gifts:
        groups = [(lab, [p for p in gifts if p["budget"] == b]) for b, lab in BUDGETS]
        groups = [(lab, ps) for lab, ps in groups if ps]
        jump = "".join(f'<a href="#{re.sub(r"[^a-z0-9]+", "-", lab.lower())}">{lab}</a>' for lab, _ in groups)
        parts.append(f'<h1 class="season">Gift picks for {today.year}</h1>'
                     '<p class="season-sub">Every pick here is one we cover in a QuickByte video: useful, '
                     'well reviewed, and something we\'d tell a friend to buy. Sorted by budget.</p>'
                     f'<nav class="jump">{jump}</nav>')
        for lab, ps in groups:
            anchor = re.sub(r"[^a-z0-9]+", "-", lab.lower())
            parts.append(f'<h2 id="{anchor}">{lab}</h2><div class="grid">{"".join(_card(p, tag) for p in ps)}</div>')
    rest = [p for p in picks if p not in gifts]
    if rest:
        parts.append(f'<h2>{"More gear from the videos" if gifts else "Gear from the videos"}</h2>'
                     f'<div class="grid">{"".join(_card(p, tag) for p in rest)}</div>')
    parts.append('<p class="fine">We earn a small commission if you buy through these links, at no extra cost '
                  'to you. Nobody pays to be on this page. Prices change often, so the ranges above are rough.</p>')

    vid_items = []
    for e in live:
        vid = videos.get(e["slug"], {}).get("video_id")
        if vid:
            vid_items.append(f'<li><a href="https://www.youtube.com/shorts/{vid}" target="_blank" rel="noopener">'
                             f'<span>{html.escape(e["title"])}</span><span>Watch</span></a></li>')
    if vid_items:
        parts.append(f'<h2>Latest videos</h2><ul class="vids">{"".join(vid_items[:12])}</ul>')

    socials = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIALS)
    title = f"{SITE_NAME} gift picks {today.year}" if gifts else f"{SITE_NAME}: gear from the videos"
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{SITE_TAGLINE}. Every product from the QuickByte videos, with links.">
<link rel="canonical" href="{SITE_URL}/">
<link rel="icon" href="logo.png">
<style>{STYLE}</style>
</head>
<body>
<div class="wrap">
<header class="head"><img src="logo.png" alt="QuickByte logo"><div>
<div class="brand">{SITE_NAME}</div><div class="tagline">{SITE_TAGLINE}</div></div></header>
<nav class="socials">{socials}</nav>
{"".join(parts)}
</div>
<footer>{SITE_NAME} &middot; @quickbytetips</footer>
</body>
</html>
"""
    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(os.path.join(DOCS_DIR, "index.html"), "w") as f:
        f.write(page)
    print(f"Built landing page: {len(picks)} picks ({len(gifts)} gift), {len(vid_items)} live videos")


if __name__ == "__main__":
    build_page()
