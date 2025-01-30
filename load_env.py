from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Check if the token is loaded correctly
if BOT_TOKEN:
    print("Token Loaded Successfully!")
else:
    print("Failed to Load Token.")
