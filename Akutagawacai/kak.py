import telebot 
from Kakugodno import API_TOKEN
from telebot.types import KeyboardButton, ReplyKeyBoardMarkup, ReplyKeyboardRemove, Message

keyboard = ReplyKeyBoardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text="Y")
button2 = KeyboardButton(text="N")
button3 = KeyboardButton(text"MB")
Keyboard.add(button)
Keyboard.add(button2)
Keyboard.add(button3)

bot = telebot.TeleBot(API_TOKEN)

STATE = 0

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """\
Обоюдно?""")

    STATE = 1


















# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")