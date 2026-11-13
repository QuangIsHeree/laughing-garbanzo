import json
from datetime import datetime, timezone
import requests

ROBLOX_API_URL = "https://games.roblox.com/v1/games?universeIds=6035872082"

def main():
    response = requests.get(ROBLOX_API_URL, timeout=10)
    response.raise_for_status()
    
    payload = {
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "data": response.json()
    }
    
    with open("version.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

if __name__ == "__main__":
    main()
