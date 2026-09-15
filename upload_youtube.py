"""
Uploads a Short to YouTube via the Data API v3 (youtube.upload scope).

One-time setup (requires the account owner - see README.md for full steps):
1. Create a Google Cloud project, enable the YouTube Data API v3.
2. Create an OAuth client ID (type: Desktop app), download it as
   client_secrets.json into this directory.
3. Run `python3 upload_youtube.py --auth-only` once. It opens a browser for
   you to grant access to your own YouTube channel and saves token.json -
   after that, uploads are fully unattended (the token auto-refreshes).

Default API quota is 10,000 units/day; each upload costs 1,600 units, so
about 6 uploads/day are possible without requesting a quota increase.
"""
import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRETS_PATH = os.path.join(SCRIPT_DIR, "client_secrets.json")
TOKEN_PATH = os.path.join(SCRIPT_DIR, "token.json")
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

SITE_URL = "https://quickbyteshorts.pages.dev"


def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_PATH):
                raise RuntimeError(
                    "client_secrets.json not found. See README.md for the one-time "
                    "Google Cloud OAuth setup - this step needs the account owner."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
    return creds


def upload_short(video_path, title, description, tags=None):
    creds = get_credentials()
    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": title[:100],
            "description": description[:5000],
            "tags": tags or [],
            "categoryId": "28",  # Science & Technology
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/mp4")
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
    return response  # contains 'id' of the uploaded video


def build_description(entry):
    lines = [entry["title"], "", "More tips + links for every video:", SITE_URL]
    if entry.get("affiliate"):
        lines += ["", "As an Amazon Associate we earn from qualifying purchases."]
    return "\n".join(lines)


if __name__ == "__main__":
    if "--auth-only" in sys.argv:
        get_credentials()
        print("Authenticated. token.json saved - future uploads are unattended.")
    else:
        print("Import and call upload_short(video_path, title, description, tags) from run_cycle.py")
