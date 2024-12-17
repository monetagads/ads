from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

# Start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Enhanced Welcome Message
    welcome_text = (
        "🕶️ *Welcome to the Cyber Portal!*\n\n"
        "🎯 Choose an option below to access exclusive resources or ads:\n\n"
        "🌟 *Features*:\n"
        "1️⃣ Neon-style buttons\n"
        "2️⃣ Dynamic links\n"
        "3️⃣ Countdown timer for anticipation\n\n"
        "🚀 Let's get started!"
    )
    
    # Inline Keyboard with Enhanced Button Design
    keyboard = [
        [
            InlineKeyboardButton("🚀 Explore ADS 1", callback_data="ads_1"),
            InlineKeyboardButton("💡 Explore ADS 2", callback_data="ads_2")
        ],
        [
            InlineKeyboardButton("🔗 Explore ADS 3", callback_data="ads_3"),
            InlineKeyboardButton("📈 Explore ADS 4", callback_data="ads_4")
        ],
        [
            InlineKeyboardButton("💬 Contact Support", url="https://t.me/YourSupportBot")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the Welcome Message with Buttons
    await update.message.reply_text(
        welcome_text, reply_markup=reply_markup, parse_mode="Markdown"
    )

# Callback Query Handler for Button Actions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Mapping callback data to links
    ads_mapping = {
        "ads_1": "https://luglawhaulsano.net/4/8666313",
        "ads_2": "https://luglawhaulsano.net/4/8666312",
        "ads_3": "https://luglawhaulsano.net/4/8666310",
        "ads_4": "https://luglawhaulsano.net/4/8666304",
    }

    if query.data in ads_mapping:
        # Loading Animation Text
        loading_text = (
            f"⏳ *Loading your ad...*\n\n"
            f"🔒 *Secure Connection Initiated*\n"
            f"🌐 *Please wait for 30 seconds...*"
        )

        # Edit message to simulate loading
        await query.edit_message_text(loading_text, parse_mode="Markdown")

        # Simulate a 30-second delay
        await asyncio.sleep(30)

        # Send the actual ad link
        await query.edit_message_text(
            f"✅ *Ad Ready!*\n\n"
            f"🔗 *Here is your link:*\n\n"
            f"[Click here to view the ad]({ads_mapping[query.data]})\n\n"
            f"Thank you for your patience! 🎉",
            parse_mode="Markdown"
        )

# Main Function to Start the Bot
def main() -> None:
    # Create the Application and Pass Your Bot Token
    application = Application.builder().token("7734607736:AAFLKIRbBEDJEWGmMO3tqKBT_vVoVGHAzpk").build()

    # Add Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Run the Bot
    application.run_polling()

if __name__ == "__main__":
    main()
