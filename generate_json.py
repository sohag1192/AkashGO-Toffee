import requests
import json
from datetime import datetime

M3U_URL = "https://raw.githubusercontent.com/BINOD-XD/Toffee-Auto-Update-Playlist/refs/heads/main/toffee_NS_Player.m3u"
OUTPUT_JSON = "toffee_formatted.json"

DEFAULT_HEADERS = {
    "Host": "bldcmprod-cdn.toffeelive.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "client-api-header": "null",
    "accept-encoding": "gzip"
}

def parse_m3u(m3u_text):
    lines = m3u_text.strip().splitlines()
    channels = []
    for i in range(len(lines)):
        if lines[i].startswith("#EXTINF"):
            # Example: #EXTINF:-1 tvg-id="id" tvg-logo="logo.png", Channel Name
            info_line = lines[i]
            link_line = lines[i+1] if i+1 < len(lines) else ""

            # Extract logo
            logo = ""
            if 'tvg-logo="' in info_line:
                logo = info_line.split('tvg-logo="')[1].split('"')[0]

            # Extract name (after comma)
            name = info_line.split(",")[-1].strip()

            channels.append({
                "category_name": "Toffee Live",
                "name": name,
                "link": link_line,
                "headers": DEFAULT_HEADERS,
                "logo": logo
            })
    return channels

def generate_formatted_json():
    print("⏳ Fetching data from:", M3U_URL)
    r = requests.get(M3U_URL)
    r.raise_for_status()

    channels = parse_m3u(r.text)

    final_json = {
        "status": "success",
        "name": "Toffee Live Channels",
        "owner": "Sohag1192",
        "Credits": "BINOD-XD",
        "channels_amount": len(channels),
        "Last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "response": channels
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)

    print(f"✅ JSON updated successfully: {OUTPUT_JSON}")
    print(f"Total channels: {len(channels)}")

if __name__ == "__main__":
    generate_formatted_json()