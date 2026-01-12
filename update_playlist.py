import requests
import json
from datetime import datetime

PLAYLIST_URL = "https://akashgo.rootmaster.xyz/?api=iptv_m3u"
OUTPUT_JSON = "AkashGo_formatted.json"
OUTPUT_M3U = "AkashGo.playlist.m3u"

def generate_formatted_playlist():
    print(f"⏳ Fetching data from: {PLAYLIST_URL}")
    try:
        response = requests.get(PLAYLIST_URL, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching playlist: {e}")
        return

    # Save raw M3U file
    with open(OUTPUT_M3U, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"📺 M3U playlist saved -> {OUTPUT_M3U}")

    # Split playlist lines
    lines = response.text.strip().splitlines()

    channels = []
    current_channel = {}

    for line in lines:
        if line.startswith("#EXTINF:"):
            # Extract channel name after comma
            try:
                name = line.split(",")[-1].strip()
            except Exception:
                name = "Unknown"
            current_channel = {"name": name, "link": ""}
        elif line.startswith("http"):
            current_channel["link"] = line.strip()
            channels.append(current_channel)
            current_channel = {}

    final_json = {
        "status": "success",
        "name": "AkashGo Playlist",
        "owner": "Sohag (formatted version)",
        "channels_amount": len(channels),
        "Last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "response": channels
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)

    print(f"✅ JSON updated successfully -> {OUTPUT_JSON}")
    print(f"📊 Total channels: {len(channels)}")

if __name__ == "__main__":
    generate_formatted_playlist()
