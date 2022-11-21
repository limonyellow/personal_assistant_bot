from telegram.ext.updater import Updater
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from bot_config import BotConfig


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Starting...")


def do(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Do nothing...")


def show_help(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
        Available Commands :
        /help - This help.
        /start - Start some.
        /do - Try to do.
        """
    )


def setup_bot(bot_config: BotConfig) -> Updater:

    updater = Updater(bot_config.bot_token.get_secret_value(), use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('do', do))
    dispatcher.add_handler(CommandHandler('help', show_help))
    return updater


def start_bot():
    config = BotConfig()
    updater = setup_bot(bot_config=config)
    if config.use_webhook:
        updater.start_webhook(
            listen=config.webhook_host,
            port=config.webhook_port,
            url_path=config.bot_token.get_secret_value(),
        )
        webhook_path = config.webhook_url + config.bot_token.get_secret_value()
        # updater.bot.setWebhook(webhook_path)
    else:
        updater.start_polling()


if __name__ == "__main__":
    start_bot()
