import json
import os
from time import sleep
from typing import List, Dict
from datetime import datetime

import requests
from colorama import Fore
from rich.console import Console
from rich.table import Table

from modules.classes import ApiError, Presence
from modules.console import log
from modules.errorhandlers import (
    handleApiError,
    handleMainLoopError,
    handleUnexpectedError,
)
from modules.notifications import notify
from modules.utils import loadConfig

# Manual mapping status
PRESENCE_TYPE_MAP = {
    0: "Offline",
    1: "Website",
    2: "In Game",
    3: "Studio",
}


def main():
    try:
        last: List[Presence] = []
        config = loadConfig()
        shouldWait: bool = False
        console = Console()

        # ===== Load local last online from file =====
        LAST_ONLINE_FILE = "last_online.json"
        if os.path.exists(LAST_ONLINE_FILE):
            with open(LAST_ONLINE_FILE, "r") as f:
                local_last_online: Dict[str, str] = json.load(f)
        else:
            local_last_online = {}

        while True:
            if len(last) != 0:
                log("***---***", Fore.WHITE)
            if shouldWait:
                sleep(10)
            shouldWait = True

            try:
                response = requests.post(
                    "https://presence.roblox.com/v1/presence/users",
                    json={"userIds": list(config.usernames.keys())},
                    cookies={".ROBLOSECURITY": config.cookie}
                    if config.loggedIn
                    else {},
                )
                _data = response.json()

                if _data.get("userPresences"):
                    presences = []
                    for i in _data["userPresences"]:
                        i.setdefault("lastOnline", None)
                        i.setdefault("userPresenceType", 0)
                        i.setdefault("lastLocation", "-")
                        i.setdefault("placeId", None)
                        i.setdefault("rootPlaceId", None)
                        i.setdefault("gameId", None)
                        i.setdefault("universeId", None)
                        i["userPresenceTypeDescription"] = PRESENCE_TYPE_MAP.get(
                            i["userPresenceType"], "Unknown"
                        )
                        presences.append(Presence(**i))
                elif _data.get("errors"):
                    errors = [ApiError(**i) for i in _data["errors"]]
                    handleApiError(errors)
                    continue

                for a in range(len(presences)):
                    current = presences[a]
                    user_id = str(current.userId)
                    username = config.usernames.get(user_id, "Unknown")

                    if len(last) != 0:
                        previous = last[a]

                        # Jika dari online ke offline, simpan waktu lokal + ke file
                        if previous.userPresenceType != 0 and current.userPresenceType == 0:
                            local_last_online[user_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            with open(LAST_ONLINE_FILE, "w") as f:
                                json.dump(local_last_online, f, indent=2)

                        if current != previous:
                            notify(config.usernames, current, False)
                    else:
                        notify(config.usernames, current, True)

                last = presences.copy()

                # ===== Show as table =====
                console.clear()
                table = Table(title="Roblox Presence Monitor")

                table.add_column("Username", style="cyan", no_wrap=True)
                table.add_column("Status", style="green")
                table.add_column("Location", style="magenta")
                table.add_column("Last Online", style="yellow")

                for presence in presences:
                    user = config.usernames.get(str(presence.userId), "Unknown")
                    status = presence.userPresenceTypeDescription
                    location = presence.lastLocation or "-"
                    user_id = str(presence.userId)
                    last_seen = local_last_online.get(user_id, "-") if presence.userPresenceType == 0 else "-"
                    table.add_row(user, status, location, last_seen)

                console.print(table)

            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.SSLError,
                json.decoder.JSONDecodeError,
            ) as e:
                handleMainLoopError(e)

    except Exception as e:
        handleUnexpectedError(e)


if __name__ == "__main__":
    main()
