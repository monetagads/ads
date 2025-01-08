from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

# Define your bot token (replace with the one provided by BotFather)
BOT_TOKEN = "7812293007:AAEsLL1hTZHESYWL7hOsYNT6CEagQlO-efA"

# Command: /start
async def start(update: Update, context):
    await update.message.reply_text(
        "Hello! 🤖\nWelcome to your Telegram Bot. Use /help to see available commands."
    )

# Command: /help
async def help_command(update: Update, context):
    await update.message.reply_text(
        "Here's what I can do:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "Just send any message and I'll reply!"
    )

# Handle normal text messages
async def handle_message(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Handle unknown commands
async def unknown_command(update: Update, context):
    await update.message.reply_text("Sorry, I didn't understand that command. 😕")

# Main function to run the bot
if __name__ == "__main__":
    # Create the bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Add a message handler for normal messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Add a fallback handler for unknown commands
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # Start polling to listen for updates
    print("Bot is running...")
    app.run_polling()
