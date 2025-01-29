from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler

app = Flask(__name__)

# Your bot token
BOT_TOKEN = "8100329499:AAHrXzFzcD3agnk6jk3cMeVE-uIMJ9TeFLw"
bot = Bot(token=BOT_TOKEN)

# Create the Application to handle updates
application = Application.builder().token(BOT_TOKEN).build()

# Example handler to process messages
async def start(update, context):
    await update.message.reply_text("Hello! I'm your bot.")

# Add handlers for different types of updates
application.add_handler(CommandHandler("start", start))

# Root URL to confirm the server is running
@app.route('/')
def index():
    return "Welcome to the bot server!"

# This is the URL where your bot will receive updates from Telegram
@app.route('/your-path', methods=['POST'])
def handle_update():
    update = Update.de_json(request.get_json(), bot)
    application.update_queue.put(update)  # Dispatch the update to the application
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the server on port 5000
