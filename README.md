# QuickByte - Automated Tech Tips Shorts Channel

Fully automated: script -> narration (edge-tts) -> stock B-roll (Pexels) ->
caption overlay (PIL + ffmpeg) -> upload (YouTube Data API v3) -> landing
page synced to GitHub Pages. $0 cost, no paid tools.

## One-time setup (needs you - none of this can be done on your behalf)

1. **Create the YouTube channel**: youtube.com -> your profile -> Create a
   channel. Name it "QuickByte" (or whatever you'd prefer - update
   `generate_landing_page.py`'s `SITE_NAME` and the `@quickbyte` handle link
   if you pick something else).

2. **Set the channel's About link** to the landing page URL once step 4 is
   live: `https://cde67.github.io/quickbyte-automation/` - this is the ONE
   clickable link Shorts viewers can actually reach (YouTube disabled
   clickable links in Shorts descriptions/comments in 2023).

3. **Google Cloud OAuth** (so uploads can run unattended):
   - console.cloud.google.com -> New Project -> name it anything.
   - APIs & Services -> Library -> enable "YouTube Data API v3".
   - APIs & Services -> OAuth consent screen -> External -> fill the required
     fields (app name "QuickByte Automation", your email) -> Save. Add your
     own Google account as a **test user** - this keeps it in "Testing" mode,
     which works fine for a single personal channel and skips Google's
     multi-week verification review.
   - Credentials -> Create Credentials -> OAuth client ID -> Application
     type: **Desktop app** -> Create -> Download JSON.
   - Save that file as `client_secrets.json` in this directory.
   - Run `python3 upload_youtube.py --auth-only` - it opens a browser, you
     approve access to your own channel, and it saves `token.json`. After
     this one time, uploads run unattended (the token auto-refreshes).

4. **GitHub repo for the landing page**: create a new **public** repo named
   `quickbyte-automation` under the same account as the other businesses,
   then enable GitHub Pages (Settings -> Pages -> Deploy from branch -> main
   -> /docs). Add a fine-grained PAT scoped to just this repo (Contents:
   Read and write) as `GITHUB_TOKEN` in `.env`.

## After setup

Run `python3 run_cycle.py` to publish one video per cycle (picks the next
unpublished script, builds the video, uploads it, updates the landing page).
Ask to have this put on a recurring schedule once you've confirmed a couple
of cycles look right.

## Adding more scripts later

Every new entry in `scripts.py` must be genuinely different in structure
from the others, not the same template with different nouns - see the
comment at the top of that file for why this matters (YouTube's inauthentic
content policy). Mix in some scripts with no `affiliate` field at all so not
every video is a product plug.
