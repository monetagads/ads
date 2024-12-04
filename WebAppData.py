from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters

def handle_webapp_data(update: Update, context: CallbackContext):
    data = update.message.web_app_data.data
    if data == '{"task":"ad_completed"}':
        update.message.reply_text("Thanks for completing the task! Your reward has been credited.")

def main():
    updater = Updater("7734607736:AAEBmRtMbDusnecfgVB7IvXvIpr524wSOE4", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.web_app_data, handle_webapp_data))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
