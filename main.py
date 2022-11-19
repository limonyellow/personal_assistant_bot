from telegram.ext.updater import Updater
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from bot_config import BotConfig


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Starting...")


def show_help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        Available Commands :-
        /help - This help.
        /start - Start some.
        """
    )


def setup_bot() -> Updater:
    config = BotConfig()
    updater = Updater(config.bot_token.get_secret_value(), use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', show_help))
    return updater


def start_bot():
    updater = setup_bot()
    updater.start_polling()


if __name__ == "__main__":
    start_bot()
