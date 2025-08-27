
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
from persiantools.jdatetime import JalaliDate

TOKEN = "8345723232:AAGNNNYZdcHG2snUUaBaa2Ss_QS-X4h3oLk"

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # تاریخ میلادی
    gregorian = datetime.now()
    gregorian_str = gregorian.strftime("%A, %B %d, %Y")

    # تاریخ شمسی
    jalali = JalaliDate.today()
    jalali_str = jalali.strftime("%A %d %B %Y")

    message = f"📅 تاریخ امروز:\n{jalali_str}\n{gregorian_str}\n\nمخصوص گروه بچه‌های ایرون @iran9897"
    await update.message.reply_text(message)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("date", date_command))
    app.run_polling()
