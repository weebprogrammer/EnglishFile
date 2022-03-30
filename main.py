import os
import telebot

TOKEN = '5195799827:AAE8qOClZgYzet9jz3SPKTogN9Nplc3Dd2Y'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def echo(message):
    bot.send_message(message.chat.id, "Hi! Im an English File audio bot. Send me a number of audio you need!")

@bot.message_handler(content_types=['text', ])
def audiosender(message):
    if os.path.exists(f'content/{message.text}.mp3') is True:
        bot.send_audio(message.chat.id, audio=open(f'content/{message.text}.mp3', 'rb'))
    else:
        bot.reply_to(message, 'check the number and try again')


bot.polling()
