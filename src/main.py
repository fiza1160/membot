import sys

import base
import initialization
import telebot
from telebot import types

try:
    bot = telebot.TeleBot(initialization.get_telegram_token())
except ValueError as err:
    print(err.args[0])
    sys.exit(1)


def get_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('❓ About')
    itembtn2 = types.KeyboardButton('📋 Show all')
    itembtn3 = types.KeyboardButton('🔥 Delete all')
    markup.add(itembtn1, itembtn2, itembtn3)
    return markup


def help_text():
    text = """\
Hi,
This is a very simple TODO bot. You can simply add any task in list, check your list or wipe it.
This bot is just few days born, so don't judge it severitly :)

And if you want so, you can participate in bot development here:  https://github.com/fiza/membot
"""
    return text


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # TODO add delete confirmation
    bot.send_message(message.chat.id, help_text(), reply_markup=get_markup())


@bot.message_handler(regexp='❓ About')
def send_welcome(message):
    bot.send_message(message.chat.id, help_text(), reply_markup=get_markup())


def is_add_request(message):
    text = message.text
    if text == '❓ About' or text == '📋 Show all' or text == '🔥 Delete all':
        return False
    return True


@bot.message_handler(func=is_add_request)
def handle_message(message):
    base.add(message.from_user.id, message.text)
    bot.send_message(message.chat.id, text='Added new task')


# TODO add inline buttons to select list item(and add buttons delete item and change item priority)
@bot.message_handler(regexp='^📋 Show all')
def handle_message(message):
    response = base.get_all(message.from_user.id)
    bot.send_message(message.chat.id, text=response)


@bot.message_handler(regexp='^🔥 Delete all')
def handle_message(message):
    base.delete_all(message.from_user.id)
    bot.send_message(message.chat.id, text='All tasks deleted')


bot.polling()
