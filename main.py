import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import jdatetime

TOKEN = "8345723232:AAGNNNYZdcHG2snUUaBaa2Ss_QS-X4h3oLk"

logging.basicConfig(level=logging.INFO)

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # تاریخ میلادی
    gregorian = datetime.now()
    gregorian_str = gregorian.strftime("%A, %B %d, %Y")

    # تاریخ شمسی
    jalali = jdatetime.datetime.now()
    jalali_str = jalali.strftime("%A %d %B %Y")

    message = f"📅 تاریخ امروز:\n{jalali_str}\n{gregorian_str}\n\nمخصوص گروه بچه‌های ایرون @iran9897"
    await update.message.reply_text(message)

if name == "main":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("date", date_command))
    app.run_polling()
