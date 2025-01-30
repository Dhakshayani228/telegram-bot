import os
import logging
import configparser
import google.generativeai as gemini
import pymongo
import aiohttp
import magic
from dotenv import load_dotenv
import os
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load Configurations
config = configparser.ConfigParser()
config.read("config.ini")

BOT_TOKEN = config["TELEGRAM"]["BOT_TOKEN"]
MONGO_URI = config["MONGODB"]["URI"]
GEMINI_API_KEY = config["GEMINI"]["API_KEY"]
SERP_API_KEY = config["SERPAPI"]["API_KEY"]

# MongoDB Setup
client = pymongo.MongoClient(MONGO_URI)
db = client['telegram_bot']
users_collection = db['users']
chat_collection = db['chat_history']
file_collection = db['file_metadata']

# Gemini AI Setup
gemini.configure(api_key=GEMINI_API_KEY)

# Logging Setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Async start function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    existing_user = users_collection.find_one({"chat_id": user.id})

    if not existing_user:
        users_collection.insert_one({
            "chat_id": user.id,
            "first_name": user.first_name,
            "username": user.username
        })
        await update.message.reply_text("Welcome! Please share your phone number.",
                                       reply_markup=ReplyKeyboardMarkup(
                                           [[KeyboardButton("Share Phone", request_contact=True)]],
                                           one_time_keyboard=True))
    else:
        await update.message.reply_text("You are already registered!")

# Async contact handler
async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    users_collection.update_one(
        {"chat_id": contact.user_id},
        {"$set": {"phone_number": contact.phone_number}}
    )
    await update.message.reply_text("Phone number registered successfully!")

# Function to interact with Gemini AI
async def gemini_chat(query):
    model = gemini.GenerativeModel("gemini-pro")  # Correct model if necessary
    response = model.generate_content(query)
    return response.text  # Ensure you're handling it correctly.

# Async message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_response = await gemini_chat(user_message)  # Await the response

    chat_collection.insert_one({
        "chat_id": update.message.chat_id,
        "user_message": user_message,
        "bot_response": chat_response,
        "timestamp": update.message.date
    })

    await update.message.reply_text(chat_response)

# Async file handler
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.photo[-1].get_file()
    file_path = await file.download()  # Ensure this is awaited

    file_type = magic.from_file(file_path, mime=True)
    analysis = await gemini_chat(f"Describe the content of this {file_type} file.")

    file_collection.insert_one({
        "chat_id": update.message.chat_id,
        "file_name": file.file_name if update.message.document else "image",
        "description": analysis
    })

    await update.message.reply_text(f"File analyzed: {analysis}")

# Async web search handler
async def web_search(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://serpapi.com/search?q={query}&api_key={SERP_API_KEY}") as response:
            data = await response.json()
            return data.get('summary', 'No summary available'), data.get('links', [])

# Async web search handling
async def handle_websearch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = " ".join(context.args)
    if not user_query:
        await update.message.reply_text("Please provide a search query.")
        return

    summary, links = await web_search(user_query)
    reply = f"Search Summary:\n{summary}\n\nTop Links:\n" + "\n".join(links)
    await update.message.reply_text(reply)

# Main function to run the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.PHOTO | filters.ATTACHMENT, handle_file))
    application.add_handler(CommandHandler("websearch", handle_websearch))

    # Fetch updates using getUpdates
    bot = Bot(token=BOT_TOKEN)
    updates = bot.get_updates()
    print("Updates fetched: ", updates)

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
