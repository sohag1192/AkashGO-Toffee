import requests
import time
from datetime import datetime

# URL of your IPTV playlist
PLAYLIST_URL = "https://akashgo.rootmaster.xyz/?api=iptv_m3u"

# Local file to save the playlist
OUTPUT_FILE = "playlist.m3u"

def update_playlist():
    try:
        print(f"[{datetime.now()}] Fetching playlist...")
        response = requests.get(PLAYLIST_URL, timeout=30)
        response.raise_for_status()  # Raise error if request failed

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"[{datetime.now()}] Playlist updated successfully -> {OUTPUT_FILE}")
    except Exception as e:
        print(f"[{datetime.now()}] Error updating playlist: {e}")

def main():
    while True:
        update_playlist()
        # Sleep for 30 minutes (1800 seconds)
        time.sleep(1800)

if __name__ == "__main__":
    main()