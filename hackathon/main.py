from constants import TOKEN
import messages
# pytelegrambotapi
import telebot
import requests
import os
from telebot import types

bot = telebot.TeleBot(TOKEN)

markup1 = types.ReplyKeyboardMarkup(row_width=2)
markup2 = types.ReplyKeyboardMarkup(row_width=2)

itembtn1 = types.KeyboardButton('Category1')
itembtn2 = types.KeyboardButton('Category2')
itembtn3 = types.KeyboardButton('Category3')
itembtn4 = types.KeyboardButton('Category4')
itembtn5 = types.KeyboardButton('Category5')
itembtn6 = types.KeyboardButton('Category6')
itembtn7 = types.KeyboardButton('Location1')
itembtn8 = types.KeyboardButton('Location2')
itembtn9 = types.KeyboardButton('Location3')
itembtn10 = types.KeyboardButton('Location4')
itembtn11 = types.KeyboardButton('Location5')
itembtn12 = types.KeyboardButton('Location6')

markup1.row(itembtn1, itembtn2, itembtn3)
markup1.row(itembtn4, itembtn5, itembtn6)

markup2.row(itembtn7, itembtn8, itembtn9)
markup2.row(itembtn10, itembtn11, itembtn12)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, messages.HELLO)

@bot.message_handler(commands = ['categories'])
def get_categories(message):
    sent1 = bot.send_message(message.chat.id, "Categories:", reply_markup=markup1)
    bot.register_next_step_handler(sent1, save1)

@bot.message_handler(commands = ['locations'])
def get_locations(message):
    sent2 = bot.send_message(message.chat.id, "Locations:", reply_markup=markup2)
    bot.register_next_step_handler(sent2, save2)

@bot.message_handler(content_types=['text'])
def handle_text(message):
	msgs = message.text
	open('saved_messages.txt' , 'a').write(msgs)
	bot.send_message(message.chat.id, 'Ваш ответ сохранён!')
	mk_dir()

def save2(message):
	location = message.text
	open('saved_messages.txt', 'a').write(location + ' || ')

def save1(message):
	category = message.text
	open('saved_messages.txt', 'a').write('\n' + str(message.from_user.first_name) + ' || ' + category + ' || ')

def mk_dir():
	with open('saved_messages.txt', "r") as f1:
		last_line = f1.readlines()[-1].split('||')
	location = last_line[2]
	category = last_line[1]
	user = last_line[0]
	msg = last_line[3]
	if not os.path.exists('/home/yerdaulet/hackathon/' + location + '/' + category + '/' + user + '/'):
		os.makedirs('/home/yerdaulet/hackathon/' + location + '/' + category + '/' + user + '/')
	with open('/home/yerdaulet/hackathon/' + location + '/' + category + '/' + user + '/messages.txt', 'w') as f:
		f.write(msg)


if __name__ == '__main__':
    print('Starting Alemresearch bot...')
    bot.polling()
