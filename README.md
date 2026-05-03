# Garena Management Telegram Bot

A Telegram bot built with Python (Flask + Telebot) to manage Garena account bindings, tokens, and info checking via external APIs.

## 🚀 Features
- **Bind Change/New Email:** Manage account security.
- **Check Bind Info:** Fetch account status, email, and mobile info.
- **Revoke Token:** Securely invalidate access tokens.
- **Webhook Integration:** Optimized for fast response times using Flask.

## 🛠 Deployment to Render

1. **Prepare the Code:**
   - Ensure your Python script is named `app.py`.
   - Update `GLOBAL_MAKER` and `GLOBAL_CHANNEL` in the script.

2. **GitHub Setup:**
   - Create a new repository and upload `app.py`, `requirements.txt`, and `render.yaml`.

3. **Render Setup:**
   - Go to [Render Dashboard](https://dashboard.render.com/).
   - Click **New +** and select **Blueprint**.
   - Connect your GitHub repository.
   - During the setup, Render will ask for the following Environment Variables:
     - `API_TOKEN`: Your Bot Token from [@BotFather](https://t.me/BotFather).
     - `WEBHOOK_URL`: Your Render App URL (e.g., `https://your-app-name.onrender.com/`).

4. **Initialize Webhook:**
   - Once the app is deployed, visit `https://your-app-name.onrender.com/` in your browser once to trigger the `bot.set_webhook()` function.

## 📝 Commands
- `/start` - Opens the main keyboard menu with all management options.

## ⚠️ Disclaimer
This tool is for educational purposes. Ensure you comply with Garena's Terms of Service when using account management APIs.

## 👤 Credits
- **Developer:** CODX GIGA
- **Channel:** @CODEX GIGA
