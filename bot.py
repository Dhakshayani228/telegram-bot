from flask import Flask
import threading

# Initialize Flask app
app = Flask(__name__)


# Home route to confirm bot is running
@app.route('/')
def home():
    return "Bot is running!"


# Function to run the Flask server
def run_flask():
    app.run(host='0.0.0.0', port=8080)


# Run Flask in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()
