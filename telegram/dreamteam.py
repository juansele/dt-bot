#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Handler

import pymongo
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

####################################################
# this one handles unknown people talking to the bot
class register_handler(Handler):
    def __init__(self):
        logger.debug('Initializing register_handler')
        self.db = pymongo.MongoClient()['dt-bot']

    def check_update(self, update):
        # check if we know the chat id
        if self.db.usuarios.find({"id_chat": update.message.chat.id}).count() == 1:
            return False
        return True

    def handle_update(self, update, dispatcher):
        if update.message.contact:
            # si es contacto, verificar si esta en la lista y agregarlo o matarlo
            usuario = self.db.usuarios.find_one({"telefono": update.message.contact.phone_number})
            if usuario:
                self.db.usuarios.update(
                    {"telefono": update.message.contact.phone_number},
                    {"$set": 
                        {"id_chat": update.message.chat.id, "accion": "idle"}
                    }
                )
                dispatcher.bot.sendMessage(update.message.chat_id, text='Todo listo %s, hablame cuando quieras hacer una visita.' % usuario['nombre'])
            else:
                dispatcher.bot.sendMessage(update.message.chat_id, text='No tengo permitido hablar con extraños.')
        else:
            # si no es contacto pedirle que nos mande el contacto
            reply_markup = ReplyKeyboardMarkup([[KeyboardButton('Compartir Información de Contacto', request_contact=True)]])
            dispatcher.bot.sendMessage(update.message.chat_id, text='Hey no te conozco!, mandame tu informacion de contacto por favor.', reply_markup=reply_markup)


##################################
# this one handles the action init
class idle_handler(Handler):
    def __init__(self):
        logger.debug('Initializing idle_handler')
        self.db = pymongo.MongoClient()['dt-bot']

    def check_update(self, update):
        # check if the chat id is currently involved in an action
        usuario = self.db.usuarios.find_one({"id_chat": update.message.chat.id})
        if usuario['accion'] == 'idle':
            return True
        return False

    def handle_update(self, update, dispatcher):
        dispatcher.bot.sendMessage(update.message.chat_id, text='Hagamos una visita')


####################################
# this one handles the state machine
class answer_handler(Handler):
    def __init__(self):
        print 'empty init'
        # do init stuff

    def check_update(self, update):
        # check update and return wether we should handle that or not
        if not isinstance(update, Update):
            return False
        return True

    def handle_update(self, update, dispatcher):
        # do the magic
        dispatcher.bot.sendMessage(update.message.chat_id, text='message handler')
