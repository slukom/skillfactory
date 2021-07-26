# Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
# Бот должен отвечать не отдельным сообщением, а с привязкой к картинке.

import telebot

TOKEN = '1824046639:AAGzpVg7r8KDmJ0-9y6woqBl44BR_nDff0E'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ['photo', ])
def repeat(message: telebot.types.Message):
   bot.reply_to(message, "Nice meme XDD")


bot.polling(none_stop=True)