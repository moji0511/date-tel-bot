import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import jdatetime
import pytz

# توکن ربات از Environment Variable
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN در Environment Variables ست نشده است!")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tz = pytz.timezone("Asia/Tehran")
    now = datetime.now(tz)

    # تاریخ میلادی
    gregorian = now.strftime("%A %d %B %Y")

    # تاریخ شمسی
    jalali = jdatetime.datetime.fromgregorian(datetime=now).strftime("%A %d %B %Y")

    msg = (
        f"📅 تاریخ امروز:\n\n"
        f"🌞 شمسی: {jalali}\n"
        f"🌍 میلادی: {gregorian}\n\n"
        f"مخصوص گروه بچه‌های ایرون @iran9897"
    )

    await update.message.reply_text(msg)

def main():
    print("🚀 Bot is starting...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("date", date_command))
    app.run_polling()

if __name__ == "__main__":
    main()
