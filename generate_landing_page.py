"""
Builds the QuickByte landing page - the one clickable link YouTube allows a
Shorts channel to surface (the channel's About/link section, since Shorts
descriptions/comments/pinned-comments are all non-clickable as of 2023).
Lists every video with its topic and, where relevant, the product mentioned.
"""
import os
import urllib.parse

import scripts as s

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")

SITE_NAME = "QuickByte"
SITE_TAGLINE = "Fast, practical tech tips - the ones that actually help"
SITE_URL = "https://quickbyteshorts.pages.dev"

STYLE = """
  :root {
    --ink: #0f1115; --accent: #ff6b4a; --accent-dark: #e34f2e;
    --bg: #fafafa; --card: #ffffff; --muted: #62666f; --border: #e8e8ea;
  }
  * { box-sizing: border-box; }
  body { font-family: -apple-system, 'Segoe UI', sans-serif; margin: 0; background: var(--bg); color: var(--ink); line-height: 1.55; }
  .wrap { max-width: 620px; margin: 0 auto; padding: 40px 20px 80px; }
  .brand { font-weight: 800; font-size: 1.6rem; letter-spacing: -0.02em; }
  .tagline { color: var(--muted); font-size: 0.95rem; margin-top: 4px; }
  .yt-link { display: inline-block; margin-top: 16px; background: var(--accent); color: #fff; text-decoration: none;
             padding: 9px 18px; border-radius: 20px; font-size: 0.9rem; font-weight: 700; }
  .yt-link:hover { background: var(--accent-dark); }
  h2 { font-size: 1rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin: 36px 0 12px; }
  .video-card { display: block; background: var(--card); border: 1px solid var(--border); border-radius: 14px;
                padding: 18px 20px; margin-bottom: 12px; }
  .video-card .vtitle { font-weight: 700; font-size: 1rem; margin: 0 0 6px; }
  .video-card .vmeta { color: var(--muted); font-size: 0.85rem; margin-bottom: 10px; }
  .video-card a.shop { display: inline-block; background: var(--ink); color: #fff; text-decoration: none;
                 padding: 7px 16px; border-radius: 18px; font-size: 0.85rem; font-weight: 600; }
  .video-card a.shop:hover { opacity: 0.85; }
  .disclosure { background: #fff5f0; border: 1px solid #ffd9c9; border-radius: 10px; padding: 12px 16px;
                font-size: 0.85rem; color: #7a3a1e; margin: 28px 0 8px; }
  footer { text-align: center; color: var(--muted); font-size: 0.85rem; padding: 30px 20px; }
"""


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


def amazon_url(item, tag):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(item)}&tag={tag}"


def build_page():
    env = load_env()
    tag = env.get("AMAZON_ASSOCIATE_TAG", "").strip() or "PLACEHOLDER-20"

    cards = []
    for entry in s.SCRIPTS:
        aff = entry.get("affiliate")
        shop_html = ""
        if aff:
            shop_html = (
                f'<a class="shop" href="{amazon_url(aff["product_name"], tag)}" '
                f'target="_blank" rel="noopener sponsored">Check price on Amazon</a>'
            )
        cards.append(f"""
        <div class="video-card">
          <p class="vtitle">{entry['title']}</p>
          <p class="vmeta">{entry['format'].replace('_', ' ').title()}</p>
          {shop_html}
        </div>""")

    disclosure = (
        '<div class="disclosure">As an Amazon Associate, we earn from qualifying purchases. '
        'Product mentions reflect genuine recommendations, not paid placements.</div>'
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE_NAME} - {SITE_TAGLINE}</title>
<meta name="description" content="{SITE_TAGLINE}. Links for every QuickByte video, all in one place.">
<link rel="canonical" href="{SITE_URL}/">
<style>{STYLE}</style>
</head>
<body>
<div class="wrap">
  <div class="brand">{SITE_NAME}</div>
  <div class="tagline">{SITE_TAGLINE}</div>
  <a class="yt-link" href="https://www.youtube.com/@quickbytetips" target="_blank" rel="noopener">Subscribe on YouTube</a>
  <h2>Videos &amp; Links</h2>
  {"".join(cards)}
  {disclosure}
</div>
<footer>{SITE_NAME}</footer>
</body>
</html>
"""
    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(os.path.join(DOCS_DIR, "index.html"), "w") as f:
        f.write(html)
    print(f"Built landing page with {len(s.SCRIPTS)} video entries in {DOCS_DIR}")


if __name__ == "__main__":
    build_page()
