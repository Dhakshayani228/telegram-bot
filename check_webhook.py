import asyncio
from telegram import Bot
import configparser

# Load your bot token from the config file
config = configparser.ConfigParser()
config.read("config.ini")
BOT_TOKEN = config["TELEGRAM"]["BOT_TOKEN"]

async def check_webhook():
    bot = Bot(token=BOT_TOKEN)  # Use the bot token from the config file
    webhook_info = await bot.get_webhook_info()  # Await the async function to get the webhook info
    print(webhook_info)  # Print the current webhook status

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(check_webhook())  # Run the check_webhook function asynchronously

