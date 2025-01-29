from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Initialize bot and updater
BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=BOT_TOKEN)

# Create an updater object
updater = Updater(bot=bot, use_context=True)

# Example command handler
def start(update, context):
    update.message.reply_text("Hello! I'm your bot.")

# Add the handler to the dispatcher
updater.dispatcher.add_handler(CommandHandler("start", start))

# Start polling to receive updates
updater.start_polling()

# Block until the user presses Ctrl+C
updater.idle()
