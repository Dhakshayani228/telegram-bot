import asyncio
from telegram import Bot

async def set_webhook():
    bot = Bot(token="8100329499:AAHrXzFzcD3agnk6jk3cMeVE-uIMJ9TeFLw")  # Replace with your actual bot token
    webhook_url = "https://341b-49-205-120-205.ngrok-free.app"  # Replace with your ngrok URL

    # Set the webhook (ensure it's awaited)
    await bot.set_webhook(url=webhook_url)
    print("Webhook has been set successfully.")

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(set_webhook())  # Run the set_webhook function asynchronously
