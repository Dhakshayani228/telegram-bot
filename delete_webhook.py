from telegram import Bot
import configparser

# Load your bot token from the config file
config = configparser.ConfigParser()
config.read("config.ini")
BOT_TOKEN = config["TELEGRAM"]["BOT_TOKEN"]

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

# Delete the webhook
bot.delete_webhook()
print("Webhook deleted successfully.")
