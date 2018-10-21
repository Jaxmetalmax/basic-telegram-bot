# -*- coding: utf-8 -*-
import sys
from time import sleep
from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import traceback
from random import randint

TOKEN = ""

bot = TelegramBot(TOKEN)

bot.update_bot_info().wait()
print (bot.username)

last_update_id = 35716035

frases = {1: "", 2: "", 3: ""}


def send_msg(bot, chat_id):
	text_msg = ""
	bot.send_message(chat_id, text_msg)


opciones = {"/command1": send_msg, "Command1": send_msg, "/Command1": send_msg}

def process_message(bot, u):

	chat_id = u.message.chat.id

	try:
		opciones[u.message.text](bot, chat_id)
	except:
		pass

while True:
#	print last_update_id
	updates = bot.get_updates(offset = last_update_id).wait()
	try:
		for update in updates:
			if int(update.update_id) > int(last_update_id):
				last_update_id = update.update_id
				process_message(bot, update)
				continue
		continue
	except Exception:
		ex = None
		print (traceback.format_exc())
		continue
