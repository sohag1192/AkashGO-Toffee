import requests
import time
from datetime import datetime

PLAYLIST_URL = "https://akashgo.rootmaster.xyz/?api=iptv_m3u"
OUTPUT_FILE = "playlist.m3u"

def update_playlist():
    try:
        print(f"[{datetime.now()}] Fetching playlist...")
        response = requests.get(PLAYLIST_URL, timeout=30)
        response.raise_for_status()

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"[{datetime.now()}] Playlist updated successfully -> {OUTPUT_FILE}")
    except Exception as e:
        print(f"[{datetime.now()}] Error updating playlist: {e}")

if __name__ == "__main__":
    update_playlist()