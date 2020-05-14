import telebot
import argparse
import os
import random

# Open cmd. Then write CD and path to bot folder.
# Run echo_bot with command 'python echo_bot.py --p "path\to\folder\"'
# Path to images folder should look like this
# "C:\photo_bot\photos\\"

parser = argparse.ArgumentParser()
parser.add_argument("--p", default=1, type=str, help="Path", required=True)
args = parser.parse_args()
path = args.p
files = os.listdir(path)

bot = telebot.TeleBot("YourBotToken")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, want a picture?")


@bot.message_handler(commands=['getcat'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')
    random.seed()
    rand_num = random.randint(0, len(files) - 1)
    img = open(path + files[rand_num], 'rb')
    bot.send_photo(message.chat.id, img,
                   reply_to_message_id=message.message_id)
    img.close()


bot.polling()
