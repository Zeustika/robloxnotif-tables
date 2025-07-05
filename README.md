# ![Logo](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/png/robloxnotif.png) [robloxnotif-tables](https://github.com/Zeustika/robloxnotif-tables)

[![GitHub](https://img.shields.io/github/license/Zeustika/robloxnotif-tables)](https://github.com/Zeustika/robloxnotif-tables/blob/main/LICENSE)
[![GitHub repo size](https://img.shields.io/github/repo-size/Zeustika/robloxnotif-tables)](https://github.com/Zeustika/robloxnotif-tables)
[![GitHub top language](https://img.shields.io/github/languages/top/Zeustika/robloxnotif-tables)](https://github.com/Zeustika/robloxnotif-tables)
[![GitHub Repo stars](https://img.shields.io/github/stars/Zeustika/robloxnotif-tables?style=social)](https://github.com/Zeustika/robloxnotif-tables/stargazers)

> **robloxnotif-tables** is a modified fork of [`jackssrt/robloxnotif`](https://github.com/jackssrt/robloxnotif) with rich-table-based UI and local last-online tracking.

---

## 📦 Supported Operating Systems

| OS            | Support | Tested             | Notifier                                                                                             |
|---------------|---------|--------------------|------------------------------------------------------------------------------------------------------|
| Windows 10    | ✅      | ✅                 | [win10toast-withsound](https://github.com/Tazmondo/Windows-10-Toast-Notifications-with-sound-option) |
| Other Windows | ❓      | ❌                 | Same as above                                                                                        |
| Linux         | ✅      | ✅ (Linux Mint 20) | [notify.py](https://pypi.org/project/notify-py/)                                                     |
| MacOS         | ❓      | ❌                 | [notify.py](https://pypi.org/project/notify-py/)                                                     |

---

## ✨ Features

- 💬 Desktop notifications (with sound)
- 🧠 Automatically saves `lastOnline` time locally (`last_online.json`)
- 🔁 Loads local lastOnline history on startup
- 📊 Clean UI using `rich.table` (terminal-based)
- 🔔 Prefix `!` or `[!]` in nicknames for custom sounds
- 🔒 Optional .ROBLOSECURITY login mode
- ✅ Works even without login (limited presence info)

---

## 🚀 How to Use

### 1. Clone the repo

```bash
git clone https://github.com/Zeustika/robloxnotif-tables.git
cd robloxnotif-tables
````

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🛠 Setup `config.json`

1. Create a file named `config.json` inside the folder
2. Paste and modify this:

```json
{
  "usernames": {
    "12345678": "!temanmu",
    "87654321": "[!]temanmu"
  },
  "loggedIn": true,
  "cookie": ".ROBLOSECURITY=YOUR_COOKIE_HERE"
}
```

* You can omit `"cookie"` or set `"loggedIn": false` if you're running in guest mode.
* The keys (`"12345678"`) are Roblox **User IDs**.
* Prefix nickname with `!` or `[!]` for sound customization.

---

## ✅ Running the App

```bash
python main.py
```

* You'll see a **real-time status table** rendered in terminal.
* Offline users will show their **last online time** from local storage.

---

## 💾 Local Last Online Tracking

* Stored in `last_online.json` next to `main.py`
* Automatically updated when user goes offline
* Persisted across restarts

Example:

```json
{
  "12345678": "2025-07-05 19:12:00",
  "87654321": "2025-07-05 18:55:10"
}
```

---

## 🔐 \[Optional] Setup `roblosecurity.jsonc`

Only needed if you want **more accurate presence info** like in-game universe ID.

1. Create a new file named `roblosecurity.jsonc`
2. Paste:

```jsonc
{
  "roblosecurity": "YOUR .ROBLOSECURITY TOKEN HERE"
}
```

⚠️ Do NOT share this file. Treat it like a password.

---

## 🪄 \[Optional] Auto Start on Windows

1. Open Task Scheduler
2. Create Basic Task
3. Trigger: "When I log on"
4. Action: "Start a program"
5. Program: `powershell.exe`
6. Arguments:

```powershell
py "D:\Path\to\robloxnotif-tables\main.py"
```

7. Start in: folder path (without quotes)

---

## 🙌 Credit

* Original project by [`@jackssrt`](https://github.com/jackssrt/robloxnotif)
* Modified by [`@Zeustika`](https://github.com/Zeustika)
* UI & local time tracking added by community forks

---

## 🔗 Discord Support

Join the original [robloxnotif Discord](https://discord.gg/6EzzURCEkB) if you need general setup help!

---

✅ **Enjoy! Now you can track your Roblox friends in a more readable, persistent, and modern way.**
