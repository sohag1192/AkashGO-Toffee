import requests
from datetime import datetime
import os

# Remote playlist URL
PLAYLIST_URL = "https://akashgo.rootmaster.xyz/?api=iptv_m3u"

# Local output file path (absolute path)
OUTPUT_FILE = "/playlist/iptv.m3u"

def update_playlist():
    try:
        print(f"[{datetime.now()}] Fetching playlist from {PLAYLIST_URL} ...")
        response = requests.get(PLAYLIST_URL, timeout=30)
        response.raise_for_status()

        # Ensure directory exists
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

        # Write playlist to file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"[{datetime.now()}] Playlist updated successfully -> {OUTPUT_FILE}")

    except Exception as e:
        print(f"[{datetime.now()}] Error updating playlist: {e}")

if __name__ == "__main__":
    update_playlist()