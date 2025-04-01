from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
import logging
from keep_alive import keep_alive

keep_alive()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")  # Replace with your Telegram user ID
print(f"TOKEN: {TOKEN}")  # Add this line after loading the environment variables

# Function to handle start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("دزولي رسائل حتى ابقى افكر منو دازهن بدال ما ادرس ههههه")

# Function to handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Forward the message to the admin (replace with your Telegram user ID)
    admin_id = ADMIN_ID  # Replace with your Telegram user ID
    await context.bot.send_message(chat_id=admin_id, text=f"Anonymous message: {update.message.text}")

    # Acknowledge the sender
    await update.message.reply_text(".")
def main():
    logger.info("Starting the bot...")

    # Set up the bot application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()
    logger.info("Bot has started.")

if __name__ == "__main__":
    main()