import telebot 
from Kakugodno import API_TOKEN
from telebot.types import KeyboardButton, ReplyKeyBoardMarkup, ReplyKeyboardRemove, Message

keyboard = ReplyKeyBoardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text="Да")
button2 = KeyboardButton(text="Нет")
button3 = KeyboardButton(text="хз")
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
    
    @bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global state
    if message.text == "Да" and state == 1:
        bot.send_message(message.from_user.id, "Ильича знаешь?")
        state = 2
    elif message.text == "Нет" and state == 1:
        bot.send_message(message.from_user.id, "Все с головой в порядке?")
        state = 3
    elif message.text == "хз" and state == 1:
        bot.send_message(message.from_user.id, "Знаешь ли ты, какова сущность мира?")
        state = 4
    elif message.text == "Да" and state == 2:
        bot.send_message(message.from_user.id, "Сдашь ЕГЭ на 95+?")
        state = 5
    elif message.text == "Нет" and state == 2:
        bot.send_message(message.from_user.id, "Ну и анлак, перезапускай")
        state = 6
    elif message.text == "Да" and state == 5:
        bot.send_message(message.from_user.id, "Ай слон")
        state = 7
    elif message.text == "Нет" and state == 5:
        bot.send_message(message.from_user.id, "Ахахахах лох")
        state = 8
    elif message.text == "хз" and state == 5:
        bot.send_message(message.from_user.id, "Даваааааай давай давай давай ты сможееееешь")
        state = 9
        


















# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\

""")
