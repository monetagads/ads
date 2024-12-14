from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Welcome Message
    welcome_text = (
        "💻 *Welcome to the Hacker Bot!*\n\n"
        "Choose an option below to proceed:"
    )
    
    # Inline Keyboard Design
    keyboard = [
        [
            InlineKeyboardButton("🟢 Open ADS 1", callback_data="ads_1"),
            InlineKeyboardButton("🟢 Open ADS 2", callback_data="ads_2")
        ],
        [
            InlineKeyboardButton("🟢 Open ADS 3", callback_data="ads_3"),
            InlineKeyboardButton("🟢 Open ADS 4", callback_data="ads_4")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send Welcome Message with Buttons
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

# Callback Query Handler for Button Actions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Handle Button Clicks
    ads_mapping = {
        "ads_1": "https://luglawhaulsano.net/4/8639415",
        "ads_2": "https://luglawhaulsano.net/4/8639413",
        "ads_3": "https://luglawhaulsano.net/4/8639353",
        "ads_4": "https://luglawhaulsano.net/4/8639412",
    }

    if query.data in ads_mapping:
        # Send a message simulating the ad with a 30-second timer
        await query.edit_message_text(
            f"🟢 Opening your ad...\n\n⏳ *Please wait for 30 seconds...*",
            parse_mode="Markdown"
        )

        # Simulate a 30-second delay
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=f"🔗 Here is your link:\n\n{ads_mapping[query.data]}"
        )

# Main Function to Start the Bot
def main() -> None:
    # Create the Application and Pass Your Bot Token
    application = Application.builder().token("YOUR_BOT_TOKEN").build()

    # Add Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Run the Bot
    application.run_polling()

if __name__ == "__main__":
    main()
