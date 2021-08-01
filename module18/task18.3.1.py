# Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение с привязкой к
# пользователю.

import telebot

TOKEN = '1824046639:AAGzpVg7r8KDmJ0-9y6woqBl44BR_nDff0E'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.username)

bot.polling(none_stop=True)