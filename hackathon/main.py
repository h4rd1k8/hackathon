from constants import TOKEN
import messages
# pytelegrambotapi
import telebot
import requests
import os
from telebot import types

bot = telebot.TeleBot(TOKEN)

markup1 = types.ReplyKeyboardMarkup(row_width=1)
markup2 = types.ReplyKeyboardMarkup(row_width=1)
markup3 = types.ReplyKeyboardMarkup(row_width=2)

itembtn1 = types.KeyboardButton('Безопасность')
itembtn2 = types.KeyboardButton('Бизнес')
itembtn3 = types.KeyboardButton('Государственное управление')
itembtn4 = types.KeyboardButton('ЖКХ')
itembtn5 = types.KeyboardButton('Здравоохранение')
itembtn6 = types.KeyboardButton('Земельные отношения')
itembtn7 = types.KeyboardButton('Инфраструктура')
itembtn8 = types.KeyboardButton('Коррупция')
itembtn9 = types.KeyboardButton('Трудовые отношения')
itembtn10 = types.KeyboardButton('Судебно-правовая система')
itembtn11 = types.KeyboardButton('Межэтнические и религиозные отношения')
itembtn12 = types.KeyboardButton('Образование')
itembtn13 = types.KeyboardButton('Общественный транспорт')
itembtn14 = types.KeyboardButton('Транспорт и автомобильные дороги')
itembtn15 = types.KeyboardButton('Экология')
itembtn16 = types.KeyboardButton('Другое')
itembtn17 = types.KeyboardButton('г. Астана')
itembtn18 = types.KeyboardButton('г. Алматы')
itembtn19 = types.KeyboardButton('Акмолинская область')
itembtn20 = types.KeyboardButton('Актюбинская область')
itembtn21 = types.KeyboardButton('Алматинская область')
itembtn22 = types.KeyboardButton('Атырауская область')
itembtn23 = types.KeyboardButton('Западно-Казахстанская область')
itembtn24 = types.KeyboardButton('Жамбылская область')
itembtn25 = types.KeyboardButton('Карагандинская область')
itembtn26 = types.KeyboardButton('Костанайская область')
itembtn27 = types.KeyboardButton('Кызылординская область')
itembtn28 = types.KeyboardButton('Мангистауская область')
itembtn29 = types.KeyboardButton('Южно-Казахстанская область')
itembtn30 = types.KeyboardButton('Павлодарская область')
itembtn31 = types.KeyboardButton('Северо-Казахстанская область')
itembtn32 = types.KeyboardButton('Восточно-Казахстанская область')
itembtn33 = types.KeyboardButton('г. Шымкент')
itembtn34 = types.KeyboardButton('Gov Service1')
itembtn35 = types.KeyboardButton('Gov Service2')
itembtn36 = types.KeyboardButton('Gov Service3')
itembtn37 = types.KeyboardButton('Gov Service4')

markup1.row(itembtn1, itembtn2, itembtn3, itembtn4)
markup1.row(itembtn5, itembtn6, itembtn7, itembtn8)
markup1.row(itembtn9, itembtn10, itembtn11, itembtn12)
markup1.row(itembtn13, itembtn14, itembtn15, itembtn16)

markup2.row(itembtn17, itembtn18, itembtn19, itembtn20)
markup2.row(itembtn21, itembtn22, itembtn23, itembtn24)
markup2.row(itembtn25, itembtn26, itembtn27, itembtn28)
markup2.row(itembtn29, itembtn30, itembtn31, itembtn32)
markup2.row(itembtn33)

markup3.row(itembtn34, itembtn35)
markup3.row(itembtn36, itembtn37)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome = bot.send_message(message.chat.id, messages.HELLO)

@bot.message_handler(commands=['category'])
def get_categories(message):
	send_c = bot.send_message(message.chat.id, 'Category', reply_markup=markup1)
	bot.register_next_step_handler(send_c, save1)
	mk_dir()

@bot.message_handler(commands=['location'])
def get_locations(message):	
	send_l = bot.send_message(message.chat.id, 'Please choose location of your report, from the following list:', reply_markup=markup2)
	bot.register_next_step_handler(send_l, save3)

@bot.message_handler(commands=['service'])
def get_gov_serv(message):
	send_gs = bot.send_message(message.chat.id, 'Government services', reply_markup=markup3)
	bot.register_next_step_handler(send_gs, save2)

def save3(message):
	location = message.text
	open('saved_messages.txt', 'a').write('\n' + str(message.from_user.username) + ' || ' + location + ' || ')

def save1(message):
	category = message.text
	open('saved_messages.txt', 'a').write(category + ' || ')

def save2(message):
	gs = message.text
	open('saved_messages.txt', 'a').write(gs + ' || ')

def mk_dir():
	with open('saved_messages.txt', "r") as f1:
		last_line = f1.readlines()[-1].split('||')
	location = last_line[1]
	category = last_line[3]
	user = last_line[0]
	gs = last_line[2]
	path = '/home/yerdaulet/hackathon/' + location + '/' + gs + '/' + str(user)
	if not os.path.exists(path):
		os.makedirs(path)
	with open(path + '/category.txt', 'w') as f:
		f.write(category)


if __name__ == '__main__':
    print('Starting Alemresearch bot...')
    bot.polling()
