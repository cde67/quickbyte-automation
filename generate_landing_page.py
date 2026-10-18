"""
Builds the QuickByte landing page (quickbyteshorts.pages.dev) - the link in the
Instagram bio and on the YouTube channel (Shorts descriptions and comments
aren't clickable, so this page is where every product link lives).

Most visitors arrive straight from the newest video, so the page opens with
that video's product ("From today's video" / "From recent videos"), then, in
gift season (mid-October through Christmas), the gift picks grouped by budget,
the rest of the gear, and the latest live videos. Each product card uses:
  - picks.json for the name, a one-line reason, the budget group and a
    permanent #pick-<slug> anchor (so a link can point straight at a card),
  - a hand-picked Pexels photo or a still from our own footage (never AI art
    or Amazon's product images), served as small WebP files,
  - a "Watch the video" link once that video is live.
Unposted scripts are never listed as videos.

Amazon Associates rules this page follows (see the Operating Agreement and
Program Policies at affiliate-program.amazon.com/help/operating/...):
  - no prices: a Site may only show prices that come live from Amazon's
    Creators API / PA API (Program Policies, Participation Requirements 2(b)),
    so cards show budget groups, never a dollar figure for a product;
  - the exact required statement "As an Amazon Associate I earn from
    qualifying purchases." (Operating Agreement section 5), placed before the
    first product link, plus a "Paid link" label next to every Amazon button
    (Amazon's help page asks for a link-level disclosure near each link);
  - plain, tagged amazon.com links (no shorteners or redirects), no star
    ratings or review counts, no Amazon logos or product images.
"""
import datetime
import html
import io
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
HANDLE = "@quickbytetips"
SOCIALS = [("YouTube", "https://www.youtube.com/@quickbytetips"),
           ("TikTok", "https://www.tiktok.com/@quickbytetips"),
           ("Instagram", "https://www.instagram.com/quickbytetips")]
BUDGETS = [(25, "Under $25"), (50, "Under $50"), (100, "Under $100"), (999, "Worth the splurge")]
# Amazon's required wording, verbatim (Operating Agreement, section 5)
ASSOCIATE_STATEMENT = "As an Amazon Associate I earn from qualifying purchases."
# "From recent videos" looks back this many live videos (about a week of
# daily posts) and shows at most RECENT_MAX products.
RECENT_LOOKBACK = 7
RECENT_MAX = 3
IMG_WIDTHS = (480, 800)


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
    items not yet resolved. Always a plain, visible amazon.com URL carrying
    our tag: Amazon forbids shorteners or redirects that hide where a link
    goes (Program Policies, Participation Requirements)."""
    link = PRODUCT_LINKS.get(item)
    if link:
        return f"{link['url']}?tag={tag}"
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(search or item)}&tag={tag}"


def _product_label(name):
    # "30W USB-C PD GaN charger" -> "30W USB-C PD GaN Charger" (keep acronyms as written)
    return " ".join(w if any(c.isupper() or c.isdigit() for c in w) else w.capitalize() for w in name.split())


def _slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def pick_slug(key, meta=None):
    """Permanent anchor slug for a product: picks.json "slug", else made from
    its display name. The card's id is "pick-<slug>"."""
    meta = meta if meta is not None else _load_json("picks.json", {}).get(key, {})
    return meta.get("slug") or _slugify(meta.get("name") or key)


def pick_url(key):
    """Deep link straight to a product's card on the landing page."""
    return f"{SITE_URL}/#pick-{pick_slug(key)}"


def pick_name(key):
    """The name a shopper recognizes (picks.json), for captions."""
    return _load_json("picks.json", {}).get(key, {}).get("name") or _product_label(key)


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
    fname = _slugify(key) + ".jpg"
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


# ---------- fast images (WebP sizes, small logo, share card) ----------

def _write_if_changed(path, data):
    """Only touch files whose bytes changed, so a rebuild doesn't create git churn."""
    if os.path.exists(path):
        with open(path, "rb") as f:
            if f.read() == data:
                return
    with open(path, "wb") as f:
        f.write(data)


def webp_variants(jpg_rel):
    """img/x.jpg -> {480: "img/x-480.webp", 800: "img/x-800.webp"} (made with
    Pillow when missing or older than the jpg). {} if Pillow can't do it."""
    try:
        from PIL import Image
    except ImportError:
        return {}
    src = os.path.join(DOCS_DIR, jpg_rel)
    out = {}
    for w in IMG_WIDTHS:
        rel = jpg_rel[:-4] + f"-{w}.webp"
        dst = os.path.join(DOCS_DIR, rel)
        if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
            try:
                with Image.open(src) as im:
                    im = im.convert("RGB")
                    if im.width != w:
                        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                    buf = io.BytesIO()
                    im.save(buf, "WEBP", quality=74, method=6)
                    _write_if_changed(dst, buf.getvalue())
            except OSError:
                return {}
        out[w] = rel
    return out


def small_logo():
    """docs/logo-112.png (the header shows the logo at 56px; the original is
    1024px). Falls back to logo.png."""
    src, dst = os.path.join(DOCS_DIR, "logo.png"), os.path.join(DOCS_DIR, "logo-112.png")
    try:
        from PIL import Image
        if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
            with Image.open(src) as im:
                buf = io.BytesIO()
                im.convert("RGB").resize((112, 112), Image.LANCZOS).save(buf, "PNG", optimize=True)
                _write_if_changed(dst, buf.getvalue())
        return "logo-112.png"
    except (ImportError, OSError):
        return "logo.png"


def _font(size, bold=True):
    from PIL import ImageFont
    cands = ([os.path.join(SCRIPT_DIR, "fonts", "Poppins-ExtraBold.ttf"), "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]
             if bold else ["/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc",
                           "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"])
    for c in cands:
        try:
            return ImageFont.truetype(c, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def share_image(headline, sub, photos):
    """docs/og.jpg, 1200x630: brand + headline on the left, a 2x2 grid of
    product photos on the right. Returns "og.jpg", or None if Pillow fails
    (the page still builds, just without a share image)."""
    try:
        from PIL import Image, ImageDraw
        W, H, M = 1200, 630, 64
        bg, ink, ink2, accent = (251, 250, 248), (20, 22, 26), (61, 66, 76), (255, 107, 74)
        img = Image.new("RGB", (W, H), bg)
        d = ImageDraw.Draw(img)
        # photo grid
        gx, gy, gap = 620, M, 14
        cell = ((W - M - gx - gap) // 2, (H - 2 * M - gap) // 2)
        for i, rel in enumerate(photos[:4]):
            with Image.open(os.path.join(DOCS_DIR, rel)) as ph:
                ph = ph.convert("RGB")
                scale = max(cell[0] / ph.width, cell[1] / ph.height)
                ph = ph.resize((round(ph.width * scale) + 1, round(ph.height * scale) + 1), Image.LANCZOS)
                left, top = (ph.width - cell[0]) // 2, (ph.height - cell[1]) // 2
                ph = ph.crop((left, top, left + cell[0], top + cell[1]))
            mask = Image.new("L", cell, 0)
            ImageDraw.Draw(mask).rounded_rectangle((0, 0, cell[0] - 1, cell[1] - 1), radius=22, fill=255)
            img.paste(ph, (gx + (i % 2) * (cell[0] + gap), gy + (i // 2) * (cell[1] + gap)), mask)
        # brand
        with Image.open(os.path.join(DOCS_DIR, "logo.png")) as lg:
            lg = lg.convert("RGB").resize((72, 72), Image.LANCZOS)
        lmask = Image.new("L", (72, 72), 0)
        ImageDraw.Draw(lmask).ellipse((0, 0, 71, 71), fill=255)
        img.paste(lg, (M, M), lmask)
        d.text((M + 88, M + 36), SITE_NAME, font=_font(34), fill=ink, anchor="lm")
        # headline (wrapped to the left column)
        f_head, y = _font(66), 210
        words, line = headline.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if d.textlength(trial, font=f_head) > gx - M - 30 and line:
                d.text((M, y), line, font=f_head, fill=ink)
                y, line = y + 80, w
            else:
                line = trial
        d.text((M, y), line, font=f_head, fill=ink)
        y += 104
        d.rectangle((M, y, M + 56, y + 6), fill=accent)
        f_sub, y = _font(28, bold=False), y + 30
        words, line = sub.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if d.textlength(trial, font=f_sub) > gx - M - 40 and line:
                d.text((M, y), line, font=f_sub, fill=ink2)
                y, line = y + 40, w
            else:
                line = trial
        d.text((M, y), line, font=f_sub, fill=ink2)
        d.text((M, H - M), "quickbyteshorts.pages.dev", font=_font(24, bold=False), fill=ink2, anchor="ls")
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=86, optimize=True, progressive=True)
        _write_if_changed(os.path.join(DOCS_DIR, "og.jpg"), buf.getvalue())
        return "og.jpg"
    except Exception as e:  # never fail the build over a share image
        print(f"  (share image skipped: {e})")
        return None


# ---------- page ----------

STYLE = """
:root{--bg:#fbfaf8;--card:#fff;--ink:#14161a;--ink2:#3d424c;--muted:#6b707a;--line:#e9e6e1;
--accent:#ff6b4a;--accent-ink:#c7401f;--chip:#f2efea;--hl:#fff3ee}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:inherit}
.wrap{max-width:980px;margin:0 auto;padding:36px 20px 72px}
.head{display:flex;align-items:center;gap:14px}
.head img{width:56px;height:56px;border-radius:50%;flex:none}
.brand{font-weight:800;font-size:1.5rem;letter-spacing:-.02em;line-height:1.1}
.tagline{color:var(--muted);font-size:.95rem}
.socials{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 0}
.socials a{text-decoration:none;font-size:.85rem;font-weight:600;padding:7px 14px;border-radius:999px;background:var(--chip)}
.socials a:hover{background:var(--line)}
.disc{color:var(--muted);font-size:.8rem;margin:16px 0 0;max-width:640px}
.kicker{display:block;color:var(--accent-ink);font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin:0 0 4px}
.latest{margin:30px 0 0}
#latest-h{margin:0 0 14px}
.latest h2{margin-top:26px}
.grid.wide{grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr))}
.feature{display:grid;grid-template-columns:1fr;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.feature .ph{aspect-ratio:4/3;background:var(--chip)}
.feature .ph img{width:100%;height:100%;object-fit:cover;display:block}
.feature .body{padding:18px 20px 20px;display:flex;flex-direction:column;gap:8px;justify-content:center}
.feature .name{margin:0;font-weight:800;font-size:1.3rem;line-height:1.25;letter-spacing:-.01em}
.feature .note{font-size:1rem;flex:none}
@media (min-width:700px){.feature{grid-template-columns:1.1fr 1fr}.feature .body{padding:26px 28px}}
.season{margin:44px 0 6px;font-size:1.75rem;font-weight:800;letter-spacing:-.02em;line-height:1.2}
.season-sub{color:var(--ink2);max-width:620px;margin:0 0 6px}
.jump{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 6px}
.jump a{text-decoration:none;font-size:.85rem;font-weight:600;padding:6px 13px;border-radius:999px;border:1px solid var(--line);background:var(--card)}
.jump a:hover{border-color:var(--ink)}
h2{font-size:1.05rem;font-weight:800;margin:36px 0 14px;letter-spacing:-.01em;scroll-margin-top:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.pick{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;scroll-margin-top:16px;transition:box-shadow .3s,border-color .3s}
.pick:target{border-color:var(--accent);box-shadow:0 0 0 3px var(--hl),0 0 0 4px var(--accent)}
.pick .ph{aspect-ratio:4/3;background:var(--chip);overflow:hidden}
.pick .ph img{width:100%;height:100%;object-fit:cover;display:block}
.pick .body{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.pick .name{font-weight:700;font-size:1.02rem;line-height:1.3;margin:0}
.seen{color:var(--muted);font-size:.82rem;margin:0}
.pick.compact{flex-direction:row}
.pick.compact .ph{aspect-ratio:auto;width:34%;max-width:170px;flex:none;position:relative}
.pick.compact .ph img{position:absolute;inset:0}
.pick.compact .body{padding:12px 14px 14px;gap:4px}
.pick.compact .name{font-size:.98rem}
.pick.compact .note{font-size:.86rem}
.pick.compact .row{margin-top:6px}
.pick.compact .watch{margin-left:0}
.note{color:var(--ink2);font-size:.92rem;flex:1;margin:0}
.row{display:flex;align-items:center;gap:6px 14px;margin-top:8px;flex-wrap:wrap}
.buy{display:inline-block;text-decoration:none;background:var(--ink);color:#fff;font-weight:700;font-size:.88rem;padding:10px 17px;border-radius:999px}
.buy:hover,.buy:focus-visible{background:var(--accent-ink)}
.paid{color:var(--muted);font-size:.72rem;letter-spacing:.02em}
.watch{font-size:.85rem;color:var(--ink2);text-decoration:underline;text-underline-offset:3px;margin-left:auto}
.fine{color:var(--muted);font-size:.82rem;margin:22px 0 0;max-width:640px}
.fine a{text-underline-offset:2px}
.vids{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}
.vids li{border-bottom:1px solid var(--line)}
.vids a{display:flex;justify-content:space-between;gap:16px;padding:13px 2px;text-decoration:none}
.vids a span:last-child{color:var(--muted);font-size:.85rem;white-space:nowrap}
.vids a:hover span:first-child{text-decoration:underline;text-underline-offset:3px}
footer{color:var(--muted);font-size:.82rem;text-align:center;padding:24px 20px 32px;max-width:680px;margin:0 auto}
footer a{color:inherit}
@media (max-width:520px){.season{font-size:1.45rem}.wrap{padding-top:26px}.feature .name{font-size:1.15rem}}
"""


def _picture(p, eager=False, sizes="(max-width:640px) calc(100vw - 40px), 320px"):
    if not p["img"]:
        return ""
    variants = webp_variants(p["img"])
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    img = (f'<img src="{p["img"]}" alt="" width="800" height="600" {load} decoding="async">')
    if not variants:
        return f'<div class="ph">{img}</div>'
    srcset = ", ".join(f"{rel} {w}w" for w, rel in sorted(variants.items()))
    return (f'<div class="ph"><picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'{img}</picture></div>')


def _buy_row(p, watch=True):
    w = (f'<a class="watch" href="{p["video"]}" target="_blank" rel="noopener">Watch the video</a>'
         if watch and p["video"] else "")
    return (f'<div class="row"><a class="buy" href="{html.escape(p["url"])}" target="_blank" '
            f'rel="sponsored nofollow noopener">See it on Amazon</a><span class="paid">Paid link</span>{w}</div>')


def _card(p, anchor=True):
    """A product card. Only the card in the main sections carries the
    #pick-<slug> id, so every anchor is unique."""
    ident = f' id="pick-{p["slug"]}"' if anchor else ""
    return f"""<article class="pick"{ident}>{_picture(p)}<div class="body">
<h3 class="name">{html.escape(p['name'])}</h3>
<p class="note">{html.escape(p['note'])}</p>
{_buy_row(p)}
</div></article>"""


def _feature(p, video_title):
    seen = f'<p class="seen">From the video: {html.escape(video_title)}</p>' if video_title else ""
    return f"""<article class="feature">{_picture(p, eager=True, sizes="(max-width:700px) calc(100vw - 40px), 500px")}<div class="body">
<h3 class="name">{html.escape(p['name'])}</h3>
{seen}<p class="note">{html.escape(p['note'])}</p>
{_buy_row(p)}
</div></article>"""


def _recent_card(p, video_title, eager=False):
    """Compact side-by-side card for the recent-videos strip, so the gift
    picks still start near the top on a phone."""
    seen = f'<p class="seen">From: {html.escape(video_title)}</p>' if video_title else ""
    return f"""<article class="pick compact">{_picture(p, eager=eager, sizes="160px")}<div class="body">
<h3 class="name">{html.escape(p['name'])}</h3>
{seen}<p class="note">{html.escape(p['note'])}</p>
{_buy_row(p)}
</div></article>"""


def _latest_section(live, picks_by_key, posted_dates, today):
    """What the visitor most likely came for: the newest live video's product
    as a big card, or, when the newest video had no product, the products
    from the last few videos."""
    recent = []  # (pick, video entry)
    for e in live[:RECENT_LOOKBACK]:
        key = (e.get("affiliate") or {}).get("product_name")
        if key in picks_by_key and key not in [p["key"] for p, _ in recent]:
            recent.append((picks_by_key[key], e))
        if len(recent) == RECENT_MAX:
            break
    if not recent:
        return ""
    newest = live[0]
    if (newest.get("affiliate") or {}).get("product_name") == recent[0][0]["key"]:
        is_today = posted_dates.get(newest["slug"]) == today.isoformat()
        title = "From today's video" if is_today else "From the latest video"
        out = [f'<section class="latest" aria-labelledby="latest-h"><h2 id="latest-h">{title}</h2>',
               _feature(recent[0][0], newest["title"])]
        if recent[1:]:
            out.append('<h2>Also from recent videos</h2><div class="grid wide">'
                       + "".join(_recent_card(p, e["title"]) for p, e in recent[1:]) + "</div>")
        return "".join(out) + "</section>"
    return ('<section class="latest" aria-labelledby="latest-h"><h2 id="latest-h">From recent videos</h2>'
            '<div class="grid wide">' + "".join(_recent_card(p, e["title"], eager=i == 0) for i, (p, e) in enumerate(recent))
            + "</div></section>")


def build_page(today=None):
    """Built for the person who just tapped "link in bio": the latest video's
    product first, then the gift picks in season, then the rest of the gear,
    then the live videos (newest first)."""
    today = today or datetime.date.today()
    env = load_env()
    tag = env.get("AMAZON_ASSOCIATE_TAG", "").strip() or "PLACEHOLDER-20"
    meta = _load_json("picks.json", {})
    posted_log = _load_json("posted_log.json", {})
    posted = posted_log.get("posted_slugs", [])
    posted_dates = posted_log.get("posted_dates", {})
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
            "key": key, "slug": pick_slug(key, m), "name": m.get("name") or _product_label(key),
            "note": m.get("note", ""), "budget": m.get("budget", 999), "gift": m.get("gift", False),
            "url": amazon_url(key, tag, aff.get("search_term")), "img": product_image(key, slugs, m.get("photo")),
            "video": f"https://www.youtube.com/shorts/{vid}" if vid else None, "live": bool(live_slug),
        })
    # live videos' picks first within each section, then by budget
    picks.sort(key=lambda p: (not p["live"], p["budget"]))
    picks_by_key = {p["key"]: p for p in picks}

    parts = [_latest_section(live, picks_by_key, posted_dates, today)]
    in_season = gift_season(today)
    gifts = [p for p in picks if p["gift"]] if in_season else []
    if gifts:
        groups = [(lab, [p for p in gifts if p["budget"] == b]) for b, lab in BUDGETS]
        groups = [(lab, ps) for lab, ps in groups if ps]
        jump = "".join(f'<a href="#{_slugify(lab)}">{lab}</a>' for lab, _ in groups)
        parts.append(f'<h1 class="season" id="gifts">Gift picks for {today.year}</h1>'
                     '<p class="season-sub">Each pick comes from a QuickByte video (a few of those videos are '
                     'still on the way). Useful things, sensibly priced, that we\'d tell a friend to buy. '
                     'Sorted by budget.</p>'
                     f'<nav class="jump" aria-label="Budgets">{jump}</nav>')
        for lab, ps in groups:
            parts.append(f'<h2 id="{_slugify(lab)}">{lab}</h2><div class="grid">{"".join(_card(p) for p in ps)}</div>')
    rest = [p for p in picks if p not in gifts]
    if rest:
        heading = "More gear from the videos" if gifts else "Gear from the videos"
        tagname = "h2" if gifts else 'h1 class="season"'
        parts.append(f'<{tagname} id="gear">{heading}</{tagname.split()[0]}>'
                     f'<div class="grid">{"".join(_card(p) for p in rest)}</div>')
    parts.append('<p class="fine">We earn a small commission if you buy through these links, at no extra cost '
                 'to you, and nobody pays to be on this page. Budget groups are based on typical prices when we '
                 'chose each pick; Amazon shows the current price. Photos show the kind of product, not always '
                 'the exact model.</p>')

    vid_items = []
    for e in live:
        vid = videos.get(e["slug"], {}).get("video_id")
        if vid:
            vid_items.append(f'<li><a href="https://www.youtube.com/shorts/{vid}" target="_blank" rel="noopener">'
                             f'<span>{html.escape(e["title"])}</span><span>Watch</span></a></li>')
    if vid_items:
        parts.append(f'<h2 id="videos">Latest videos</h2><ul class="vids">{"".join(vid_items[:12])}</ul>')

    # ---- head: SEO, social share card, structured data ----
    if gifts:
        title = f"Tech gift ideas {today.year}: useful picks under $25, $50 and $100 | {SITE_NAME}"
        desc = (f"Practical tech gifts for {today.year} from the {SITE_NAME} videos, sorted by budget: "
                "chargers, trackers, earbuds, an e-reader and more, each with a plain reason it made the list.")
        og_head, og_sub = f"Gift picks for {today.year}", "Useful tech, sorted by budget, from the QuickByte videos"
    else:
        title = f"{SITE_NAME}: the gear from the videos"
        desc = f"{SITE_TAGLINE}. Every product from the {SITE_NAME} videos, with a plain reason for each."
        og_head, og_sub = "Gear from the videos", "Which tech is worth buying, and which isn't"
    listed = gifts + rest
    # share card: one photo per budget group first, so it shows a spread of gifts
    firsts = [next((p for p in listed if p["budget"] == b and p["img"]), None) for b, _ in BUDGETS]
    og_photos = [p["img"] for p in firsts if p] + [p["img"] for p in listed if p["img"] and p not in firsts]
    og = share_image(og_head, og_sub, og_photos)
    logo = small_logo()
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{SITE_URL}/#website", "name": SITE_NAME, "url": f"{SITE_URL}/",
         "description": SITE_TAGLINE},
        {"@type": "ItemList", "name": og_head, "numberOfItems": len(listed),
         "itemListElement": [{"@type": "ListItem", "position": i, "name": p["name"],
                              "url": f"{SITE_URL}/#pick-{p['slug']}"} for i, p in enumerate(listed, start=1)]},
    ]}
    og_tags = ""
    if og:
        og_tags = (f'<meta property="og:image" content="{SITE_URL}/{og}">\n'
                   '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
                   f'<meta property="og:image:alt" content="{html.escape(og_head)} from {SITE_NAME}">\n'
                   '<meta name="twitter:card" content="summary_large_image">\n'
                   f'<meta name="twitter:image" content="{SITE_URL}/{og}">\n')

    socials = "".join(f'<a href="{u}" target="_blank" rel="noopener me">{n}</a>' for n, u in SOCIALS)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE_URL}/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#fbfaf8">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{html.escape(og_head)} | {SITE_NAME}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE_URL}/">
{og_tags}<link rel="icon" href="{logo}">
<link rel="apple-touch-icon" href="logo.png">
<style>{STYLE}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")}</script>
</head>
<body>
<div class="wrap">
<header class="head"><img src="{logo}" alt="QuickByte logo" width="56" height="56"><div>
<div class="brand">{SITE_NAME}</div><div class="tagline">{SITE_TAGLINE}</div></div></header>
<nav class="socials" aria-label="QuickByte on social media">{socials}</nav>
<p class="disc">The Amazon links on this page are affiliate links. {ASSOCIATE_STATEMENT}</p>
<main>
{"".join(parts)}
</main>
</div>
<footer>{SITE_NAME} &middot; {HANDLE}<br>{ASSOCIATE_STATEMENT} Amazon and the Amazon logo are trademarks of
Amazon.com, Inc. or its affiliates. <a href="privacy.html">Privacy</a></footer>
</body>
</html>
"""
    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(os.path.join(DOCS_DIR, "index.html"), "w") as f:
        f.write(page)
    print(f"Built landing page: {len(picks)} picks ({len(gifts)} gift), {len(vid_items)} live videos")


if __name__ == "__main__":
    build_page()
