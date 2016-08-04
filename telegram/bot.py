#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dreamteam

from telegram import (ReplyKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler)

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("198643176:AAExGlD7Msdj9i62E6x36Vlt3JU3IoaOBlQ")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    dtRegHandler = dreamteam.register_handler()
    dtIdleHandler = dreamteam.idle_handler()
    dtHandler = dreamteam.DTHandler()

    dp.add_handler(dtRegHandler)
    dp.add_handler(dtIdleHandler)
    dp.add_handler(dtHandler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
