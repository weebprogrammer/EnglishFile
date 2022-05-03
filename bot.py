import os
import telebot
from config import BOTTOKEN, DISKTOKEN
import yadisk


bot = telebot.TeleBot(BOTTOKEN)
disk = yadisk.YaDisk(token=DISKTOKEN)


@bot.message_handler(commands=['start', 'help'])
def echo(message):
    bot.send_message(message.chat.id, "Hi! Im an English File audio bot. Send me a number of audio you need!")


def namecheck(mssg: str):
    for audio in list(disk.listdir('/englishfile')):
        if audio['name'] == mssg:
            return True


@bot.message_handler(content_types=['text', ])
def main(message):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(message.from_user.first_name+'\n')

    if namecheck(message.text+'.mp3') is True:
        disk.download('/englishfile/'+message.text+'.mp3', f'cache/{message.text}.mp3')
        bot.send_audio(message.chat.id, audio=open(f'cache/{message.text}.mp3', 'rb'))
        os.remove(f'cache/{message.text}.mp3')
    else:
        bot.reply_to(message, 'check the number and try again')




if __name__ == "__main__":

    bot.polling(none_stop=True)
