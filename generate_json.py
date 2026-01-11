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

def generate_formatted_json():
    print("⏳ Fetching data from:", M3U_URL)
    r = requests.get(M3U_URL)
    r.raise_for_status()

    try:
        raw_channels = json.loads(r.text)
    except json.JSONDecodeError as e:
        print("❌ Error: File is not valid JSON.\n", e)
        return

    response_data = []
    for ch in raw_channels:
        response_data.append({
            "category_name": "Toffee Live",
            "name": ch.get("name", ""),
            "link": ch.get("link", ""),
            "headers": {
                **DEFAULT_HEADERS,
                "cookie": ch.get("cookie", "")
            },
            "logo": ch.get("logo", "")
        })

    final_json = {
        "status": "success",
        "name": "Toffee Live Channels",
        "owner": "Sohag & Credits: BINOD-XD",
        "channels_amount": len(response_data),
        "Last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "response": response_data
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)

    print(f"✅ JSON updated successfully: {OUTPUT_JSON}")
    print(f"Total channels: {len(response_data)}")

if __name__ == "__main__":
    generate_formatted_json()