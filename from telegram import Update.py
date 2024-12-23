from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import json

# Load or initialize user data
user_data_file = "user_data.json"
try:
    with open(user_data_file, "r") as file:
        user_data = json.load(file)
except FileNotFoundError:
    user_data = {}

# Save user data to file
def save_user_data():
    with open(user_data_file, "w") as file:
        json.dump(user_data, file)

# Start command
def start(update: Update, context: CallbackContext):
    chat_id = str(update.effective_chat.id)
    if chat_id not in user_data:
        user_data[chat_id] = {"name": "", "watched_ads": 0, "coins": 0}
        update.message.reply_text("Welcome! Please enter your name:")
    else:
        user = user_data[chat_id]
        update.message.reply_text(f"Welcome back, {user['name']}! You've watched {user['watched_ads']} ads and earned {user['coins']} coins.")

# Handle user name input
def name_handler(update: Update, context: CallbackContext):
    chat_id = str(update.effective_chat.id)
    if chat_id in user_data and not user_data[chat_id]["name"]:
        user_data[chat_id]["name"] = update.message.text
        save_user_data()
        update.message.reply_text(f"Thanks, {user_data[chat_id]['name']}! You can start watching ads with /watch.")

# Watch ad command
def watch_ad(update: Update, context: CallbackContext):
    chat_id = str(update.effective_chat.id)
    if chat_id in user_data:
        user_data[chat_id]["watched_ads"] += 1
        user_data[chat_id]["coins"] += 2
        save_user_data()
        update.message.reply_text(f"Ad watched! You now have {user_data[chat_id]['coins']} coins.")
    else:
        update.message.reply_text("Please start with /start to register.")

# Main function to run the bot
def main():
    TOKEN = "7734607736:AAFLKIRbBEDJEWGmMO3tqKBT_vVoVGHAzpk"  # Replace with your bot token
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("watch", watch_ad))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, name_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
