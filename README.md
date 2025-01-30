 Description for your project:
# Telegram AI Chatbot

## Overview
The **Telegram AI Chatbot** is an interactive bot that leverages the **Gemini API** for AI-powered responses, along with MongoDB for data storage. This bot can register users, provide conversational responses, analyze image/file content, and perform web searches—all within the Telegram environment.

### Features:
- **User Registration**: Saves the user's `first_name`, `username`, and `chat_id` in MongoDB upon the first interaction. It also requests the user's phone number via the contact button and stores it in the database.
  
- **Gemini-Powered Chat**: Uses Google's free **Gemini API** to provide answers to user queries and stores the chat history (user input + bot response) in MongoDB with timestamps.

- **Image/File Analysis**: The bot accepts images/files (e.g., JPG, PNG, PDF), uses Gemini to analyze their content, and provides a description of the content. The file metadata is saved in MongoDB.

- **Web Search**: Users can initiate a web search by typing `/websearch`. The bot will search the web using an AI agent and provide a summarized response along with top web links.

## Requirements

To run this project locally, you'll need to have the following installed:
- Python 3.6+
- MongoDB (local or cloud instance like MongoDB Atlas)
- Telegram Bot API token (you can create your own bot using [BotFather](https://core.telegram.org/bots#botfather))

### Install Required Python Packages:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
- Flask: For web framework to handle the bot's requests.
- python-telegram-bot: To interact with the Telegram Bot API.
- pymongo: To interact with MongoDB.
- google-generativeai: For Gemini-powered AI responses.
- requests: For HTTP requests when needed.

## Setup Instructions

1. **Set Up MongoDB**:
   - You can use either a local MongoDB server or a cloud instance (MongoDB Atlas).
   - Make sure to update the MongoDB URI in the code to match your setup.

2. **Get Your Telegram Bot Token**:
   - Create your own bot using [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
   - Once the bot is created, you'll receive a bot token. Replace the `BOT_TOKEN` value in the code with your token.

3. **Gemini API Access**:
   - Use the **Google Generative AI API (Gemini)** to enable AI-powered conversations. You can access it via the `google.generativeai` Python library.
   - Replace the API key in the code with your Gemini API key if necessary.

4. **Running the Bot**:
   - After setting everything up, run the following command to start the Flask web server:
     ```bash
     python script.py
     ```
   - This will run the bot on a local server (usually `http://127.0.0.1:5000/`).

5. **Deploying the Bot (Optional)**:
   - If you want to deploy your bot to a cloud platform (like Heroku, Replit, or AWS), follow their respective deployment guides.
   - Make sure to configure your server's webhook to receive updates from Telegram.

## How It Works

1. **User Registration**:
   - When a user starts interacting with the bot, it registers them by saving their `first_name`, `username`, and `chat_id` in MongoDB.
   - The bot requests the user’s phone number through Telegram's contact button and stores it in the database.

2. **Gemini-Powered Chat**:
   - Whenever a user sends a message, the bot queries the Gemini API to generate a response and stores both the user input and bot response in MongoDB.

3. **Image/File Analysis**:
   - If a user sends an image/file, the bot uses Gemini to analyze and describe the content. Metadata like filename and description are saved in MongoDB.

4. **Web Search**:
   - If the user types `/websearch`, the bot prompts them for a query and returns an AI-powered summary of the top web search results.

## MongoDB Storage

- **User Registration**: 
   - The bot stores user details like their phone number, username, and chat ID.
  
- **Chat History**: 
   - The bot stores each conversation (user input + bot response) with timestamps.

- **Image/File Metadata**: 
   - For each image/file sent by the user, the bot saves metadata like filename and description.

