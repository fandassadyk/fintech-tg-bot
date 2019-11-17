import telebot

bot = telebot.TeleBot('1055317931:AAFMyToRCKY7mFcMHvpc5JfStK5xpUuu4RA')

@bot.message_handler(commands=['start'])
#@bot.message_handler(content_types=['text', 'document', 'audio'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет, соскучился?')


bot.polling()
