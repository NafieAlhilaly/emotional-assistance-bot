import os
import telebot
from dotenv import load_dotenv
from quotes import RandomQuotes
from gifs import RandomGifs

load_dotenv()
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

rq = RandomQuotes()
rg = RandomGifs()


@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, "Hey there beautiful 😍, how can i help you ?")


@bot.message_handler(commands=["hi"])
def hi(message):
    bot.send_message(message.chat.id, "Hey")


@bot.message_handler(commands=["quote"])
def quotes(message):
    bot.send_message(message.chat.id, "Ok, finding the best quote for you 😉 ...")
    bot.send_message(message.chat.id, rq.get_random_quote())


@bot.message_handler(commands=["hug"])
def quotes(message):
    bot.send_message(message.chat.id, "Ok, come closer 🤗")
    bot.send_message(message.chat.id, rg.get_random_hug_gif())


bot.infinity_polling(timeout=10, long_polling_timeout=5)