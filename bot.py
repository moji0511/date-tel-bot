import logging
from telegram.ext import Application

TOKEN = "8345723232:AAGNNNYZdcHG2snUUaBaa2Ss_QS-X4h3oLk"

logging.basicConfig(level=logging.INFO)

def main():
    print("🚀 Bot is starting...")
    app = Application.builder().token(TOKEN).build()
    app.run_polling()

if __name__ == "__main__":
    main()
