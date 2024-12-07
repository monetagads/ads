from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Command to provide Mini App link
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Open Mini App", web_app={"url": "https://monetagads.github.io/ads/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Click below to open the Mini App:", reply_markup=reply_markup)

def main():
    # Replace 'YOUR_TOKEN' with your BotFather token
    updater = Updater("7734607736:AAEBmRtMbDusnecfgVB7IvXvIpr524wSOE4", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
