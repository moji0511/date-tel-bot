import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
from khayyam import JalaliDatetime
import pytz

# توکن ربات
TOKEN = "8345723232:AAGNNNYZdcHG2snUUaBaa2Ss_QS-X4h3oLk"

# لاگ‌گیری
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# دستور /date
async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tz = pytz.timezone("Asia/Tehran")

    # تاریخ میلادی
    gregorian = datetime.now(tz).strftime("%A %d %B %Y")

    # تاریخ شمسی
    jalali = JalaliDatetime.now().strftime("%A %d %B %Y")

    msg = (
        f"📅 تاریخ امروز:\n\n"
        f"🌞 شمسی: {jalali}\n"
        f"🌍 میلادی: {gregorian}\n\n"
        f"مخصوص گروه بچه‌های ایرون @iran9897"
    )

    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("date", date_command))
    app.run_polling()

if __name__ == "__main__":
    main()
