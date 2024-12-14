from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("ADS 1", url="https://luglawhaulsano.net/4/8639415")],
        [InlineKeyboardButton("ADS 2", url="https://luglawhaulsano.net/4/8639413")],
        [InlineKeyboardButton("ADS 3", url="https://luglawhaulsano.net/4/8639353")],
        [InlineKeyboardButton("ADS 4", url="https://luglawhaulsano.net/4/8639412")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose an option:", reply_markup=reply_markup)

def main():
    updater = Updater("7583196010:AAGXKsZt55IGeVddXJPMBFwxj---NJDt2fQ", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
