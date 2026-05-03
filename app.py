import os
import requests
from flask import Flask, request
import telebot
from telebot import types

# --- CONFIGURATION ---
API_TOKEN = os.environ.get("BOT_TOKEN")  # सुरक्षित (use Render env variable)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # your Render app URL

if not API_TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

GLOBAL_MAKER = "CODX GIGA"
GLOBAL_CHANNEL = "@CODEX GIGA"

# --- FUNCTIONS ---

def is_success(rsp):
    if rsp.status_code != 200:
        return False
    try:
        rj = rsp.json()
        return rj.get("success", False)
    except:
        return False

def format_res(rsp_json):
    try:
        error_msg = rsp_json.get('error')
        if error_msg:
            return f"❌ Failed! Error: {error_msg}"
        return f"✅ Success!\n👤 Dev: {GLOBAL_MAKER}\n📢 Channel: {GLOBAL_CHANNEL}"
    except:
        return "❌ Failed! Invalid Response"

# --- BOT COMMANDS ---

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('Check Bind Info'),
        types.KeyboardButton('Revoke Token')
    )
    bot.send_message(message.chat.id, "Welcome!", reply_markup=markup)

# --- CHECK INFO ---

@bot.message_handler(func=lambda m: m.text == 'Check Bind Info')
def ask_token_check(message):
    msg = bot.send_message(message.chat.id, "Send Access Token:")
    bot.register_next_step_handler(msg, process_check_info)

def process_check_info(message):
    access = message.text
    url = "https://bindinfocrownx612.vercel.app/check"

    try:
        rsp = requests.get(url, params={'access_token': access})
        if is_success(rsp):
            data = rsp.json().get("data", {})
            res = (
                f"📊 Status: {data.get('status')}\n"
                f"📧 Email: {data.get('email')}\n"
                f"📱 Mobile: {data.get('mobile')}"
            )
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, format_res(rsp.json()))
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")

# --- REVOKE ---

@bot.message_handler(func=lambda m: m.text == 'Revoke Token')
def ask_token_revoke(message):
    msg = bot.send_message(message.chat.id, "Send token to revoke:")
    bot.register_next_step_handler(msg, process_revoke)

def process_revoke(message):
    access = message.text
    url = "https://crownxrevoker73.vercel.app/revoke"

    try:
        rsp = requests.get(url, params={'access_token': access})
        bot.send_message(message.chat.id, format_res(rsp.json()))
    except:
        bot.send_message(message.chat.id, "Request failed")

# --- WEBHOOK ---

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook_handler():
    json_data = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/")
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{API_TOKEN}")
    return "Webhook set!", 200

# --- RUN ---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))