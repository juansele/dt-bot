#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import Update
from telegram.ext import Handler

class DTHandler(Handler):
    def __init__(self):
        print 'empty init'
        # do init stuff

    def check_update(self, update):
        # check update and return wether we should handle that or not
        if not isinstance(update, Update):
            return False

        user = None
        chat = None

        if update.message:
            user = update.message.from_user
            chat = update.message.chat

        elif update.edited_message:
            user = update.edited_message.from_user
            chat = update.edited_message.chat

        elif update.inline_query:
            user = update.inline_query.from_user

        elif update.chosen_inline_result:
            user = update.chosen_inline_result.from_user

        elif update.callback_query:
            user = update.callback_query.from_user
            chat = update.callback_query.message.chat if update.callback_query.message else None

        else:
            return False

        print user, chat

        return True

    def handle_update(self, update, dispatcher):
        # do the magic
        dispatcher.bot.sendMessage(update.message.chat_id, text='va bien!')
