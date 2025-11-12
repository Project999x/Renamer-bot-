# 👮‍♂️ SaveRestricted - Telegram Media Saver Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width="250">
  </a>
</p>

## 🧠 About The Bot

**SaveRestricted** is a lightweight Telegram bot designed to help users **save restricted or view-once media** from both **private** and **public** chats.

🔐 No extra features — just clean saving.  

💾 Supports:
- 📥 Downloading photos, videos, and files from any chat  
- 🔐 Save restricted content (view-once / protected)  
- 🧑‍💻 User login/logout  
- 📁 Batch media saving from chats  

---

## 🛠 Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| 🐍 Python    | Core Programming Language        |
| 📦 Pyrogram  | Telegram API Client              |
| 🍃 MongoDB   | User login state storage         |
| ⚙️ Aiogram   | Command handling (optional)      |

---

## 🚀 Demo Bot

🔗 Try it here: [@SaveRestrictedBot](https://t.me/resavesbot)

> 🛠 Developed by: [NyxKing](https://t.me/Shizukawachan)

---

## 🔑 Features

- 👤 **Login/Logout System**  
  - Secure session management for users

- 🗂 **Download From Any Chat**  
  - Save from private or public messages

- 🧾 **Batch Save Support**  
  - Forward multiple messages and download all media in one go

- 📌 Minimal, fast, and stable

---

## 🧪 Bot Commands

| Command     | Description                    |
|-------------|--------------------------------|
| `/start`    | Start the bot                  |
| `/login`    | Authenticate yourself          |
| `/logout`   | Logout your session            |
| `/batch`    | Send multiple messages to save |

---

## 🌱 Environment Variables

| Variable        | Description                    |
|-----------------|--------------------------------|
| `API_HASH`      | Telegram API hash              |
| `APP_ID`        | Telegram API ID                |
| `BOT_TOKEN`     | Bot Token from BotFather       |
| `DB_URL`        | MongoDB connection string      |
| `DB_NAME`       | MongoDB DB name                |

---

## 🚀 Deployment

### 🖥️ Local
```bash
git clone https://github.com/
cd save-restricted
pip3 install -r requirements.txt
python3 main.py
