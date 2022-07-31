
# import os
# from telegram import Update

# from telegram.ext import (
#     Updater,
#     CommandHandler,
#     CallbackContext,
#     ConversationHandler,
#     Filters
# )

# from ticker import get_price_change

# TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "Not Available")

# def get_px_change(
#     update: Update,
#     context: CallbackContext,
#     ticker: str = None,
# ) -> None:
    
#     # assumes command is passed via `/get_px_change AMZN` and only
#     # a single ticker is accepted
#     ticker = update.message.text.split("/get_px_change")[1].strip()

#     # use our script to obtain price change
#     pct_chng, _ = get_price_change(ticker)
#     message = f"{ticker.upper()} changed by {pct_chng}!"
    
#     update.message.reply_text(message)


# def main() -> None:
#     updater = Updater(TOKEN)

#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher

#     # Add handlers here
#     dispatcher.add_handler(CommandHandler("get_px_change", get_px_change))

#     # # Start the Bot
#     # updater.start_polling()

#     # # Block until the user presses Ctrl-C or the process receives SIGINT,
#     # # SIGTERM or SIGABRT. This should be used most of the time, since
#     # # start_polling() is non-blocking and will stop the bot gracefully.
#     # updater.idle()

#     # Start the Bot
#     # `start_polling` for local dev; webhook for production
#     # updater.start_polling()
#     updater.start_webhook(listen="0.0.0.0",
#         port=int(os.environ.get('PORT', 5000)),
#         url_path=TOKEN,
#         webhook_url='https://stockbot-telegram.herokuapp.com/' + TOKEN
#         # webhook_url="https://api.telegram.org/bot" + TOKEN + "/setWebhook?url=https://stockbot-telegram.herokuapp.com"
#     )
#     # updater.bot.setWebhook("https://api.telegram.org/bot" + TOKEN + "/setWebhook?url=https://stockbot-telegram.herokuapp.com")
#     # webhook_url='https://myapp.herokuapp.com/' + SECRET_KEY
    
#     updater.idle()


# if __name__ == "__main__":
#     main()