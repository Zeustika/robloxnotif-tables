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


## 🛠️ Setup

If you need help setting up **robloxnotif-tables**, feel free to [join the Discord server!](https://discord.gg/6EzzURCEkB)

### ✅ Step-by-Step

1. **Download and install [Python 3](https://www.python.org/downloads/)**
   Make sure Python is added to your system PATH.

2. **Clone or download the repository**

   ```bash
   git clone https://github.com/Zeustika/robloxnotif-tables.git
   cd robloxnotif-tables
   ```

3. **Install the dependencies**

   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Create a configuration file**
   Make a file named `config.json` in the same folder as `main.py`. Paste this:

   ```jsonc
   {
     "usernames": {
       // Hi! I'm a comment. You can use me to organize users.
       "PERSON_1_USERID": "PERSON 1 NICKNAME",
       "PERSON_2_USERID": "PERSON 2 NICKNAME",
       "PERSON_3_USERID": "[!]Important Person"
     },
     "loggedIn": true,
     "cookie": ".ROBLOSECURITY=YOUR_COOKIE_HERE"
   }
   ```

   * You can add more than 3 people.
   * You can comment lines because this file supports JSONC format.
   * If you are not using login, set `"loggedIn": false`.

5. **Customize the values**
   Replace the placeholder text with real values:

   ```json
   {
     "usernames": {
       // Roblox Admins
       "1": "!ROBLOX",
       "156": "real builderman",
       // Friends
       "261": "[!]cool dude"
     },
     "loggedIn": true,
     "cookie": ".ROBLOSECURITY=_|WARNING:-DoNotShareThis"
   }
   ```

6. **Run the script**

   ```bash
   python main.py
   ```

   or

   ```bash
   py main.py
   ```

   depending on your system configuration.

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
