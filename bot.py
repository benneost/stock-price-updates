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

# updater = Updater(token=TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # set up the introductory statement for the bot when the /start command is invoked
# def start(update, context):
#     chat_id = update.effective_chat.id
#     context.bot.send_message(chat_id=chat_id, text="Hello there. Provide any Ticker and I will give you a bunch "
#                                                 "of information about it.")

# def get_px_change(
#     update: Update,
#     context: CallbackContext,
#     ticker: str = None,
# ) -> None:
    
#     # assumes command is passed via `/get_px_change AMZN` and only
#     # a single ticker is accepted
#     ticker = update.message.text

#     # use our script to obtain price change
#     pct_chng, _ = get_price_change(ticker)
#     message = f"{ticker.upper()} changed by {pct_chng}!"
    
#     update.message.reply_text(message)

# # run the start function when the user invokes the /start command 
# dispatcher.add_handler(CommandHandler("start", start))

# dispatcher.add_handler(MessageHandler(Filters.text, get_px_change))
# updater.start_webhook(listen="0.0.0.0",
#     port=int(os.environ.get('PORT', 5000)),
#     url_path=TOKEN,
#     webhook_url='https://stockbot-telegram.herokuapp.com/' + TOKEN
# )

# updater.idle()