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

class neodim():
    def __init__(self):
        logger.debug('Initializing neodim_checker')
        self.db = pymongo.MongoClient()['dt-bot']

    def check(self, update):
        print 'check'

    def process(self, update):
        print 'process'

    def read(self, update):
        print 'read'
