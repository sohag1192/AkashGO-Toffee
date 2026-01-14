import requests
import json
from datetime import datetime

PLAYLIST_URL = "https://akashgo.rootmaster.xyz/?api=iptv_m3u"
OUTPUT_JSON = "AkashGo_formatted.json"

def generate_formatted_json():
    print(f"⏳ Fetching data from: {PLAYLIST_URL}")
    try:
        response = requests.get(PLAYLIST_URL, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching playlist: {e}")
        return

    lines = response.text.strip().splitlines()

    channels = []
    current_channel = {}

    for line in lines:
        if line.startswith("#KODIPROP:"):
            # Kodi property line, split into key/value
            try:
                key, value = line.replace("#KODIPROP:", "").split("=", 1)
                current_channel[key.strip()] = value.strip()
            except Exception:
                pass

        elif line.startswith("#EXTINF:"):
            # Extract attributes from EXTINF line
            try:
                # Example: #EXTINF:-1 tvg-id="1" tvg-name="BPL" ...
                parts = line.split(",")
                info = parts[0]
                name = parts[-1].strip()

                # Parse attributes like tvg-id, tvg-name, tvg-logo, group-title
                attrs = {}
                for token in info.split(" "):
                    if "=" in token:
                        k, v = token.split("=", 1)
                        attrs[k.strip()] = v.strip().strip('"')

                current_channel.update(attrs)
                current_channel["name"] = name
            except Exception:
                current_channel["name"] = "Unknown"

        elif line.startswith("http"):
            # Stream link
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
    generate_formatted_json()