import telebot
import requests
import json

bot = telebot.TeleBot('1065718707:AAGpjiJBzaFTpwz0P_bhgMi7qRS1qO871Js')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20191117T205104Z.3ecf8e2efab662cd.262088c507c9012d2a5895fcfbc5624a17dd65ac'
    text = message.text
    lang = 'ru-en'

    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    result = json.loads(r.text)
    result1 = ' '.join(result['text'])
    bot.send_message(message.from_user.id, result1)


bot.polling(none_stop=True, interval=0)
