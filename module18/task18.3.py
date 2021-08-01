import telebot

TOKEN = '1824046639:AAGzpVg7r8KDmJ0-9y6woqBl44BR_nDff0E'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ['voice'])
def repeat(message: telebot.types.Message):
   bot.send_message(message.chat.id, "У тебя красивый голос")

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, "Привет, " + message.chat.username)

bot.polling(none_stop=True)