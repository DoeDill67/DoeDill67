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
    elif message.text == "Да" and state == 3:
        bot.send_message(message.from_user.id, "Справка от психолога есть?")
        state = 10
    elif message.text == "Нет" and state == 3:
        bot.send_message(message.from_user.id, "Люди в халатах едут, не беспокойся")
        state = 11
    elif message.text == "хз" and state == 3:
        bot.send_message(message.from_user.id, "Нууу ладно, но люди в халатах запомнили")
        state = 12
    elif message.text == "Да" and state == 10:
        bot.send_message(message.from_user.id, "Тогда наш слон")
        state = 13
    elif message.text == "Нет" and state == 10:
        bot.send_message(message.from_user.id, "Понял тебя, УАЗ буханка выгодно алабуга")
        state = 14
    elif message.text == "хз" and state == 10:
        bot.send_message(message.from_user.id, "К тебе или ко мне? риторический вопрос")
        state = 15
    elif message.text == "Да" and state == 4:
        bot.send_message(message.from_user.id, "Фига ты философ")
        state = 16
    elif message.text == "Нет" and state == 4:
        bot.send_message(message.from_user.id, "Нарвал получается")
        state = 17
    elif message.text == "хз" and state == 4:
        bot.send_message(message.from_user.id, "я тоже")
        state = 18
    else:
        bot.send_message(message.from_user.id, "Бро только кнопки можно нажимать нет свободы слова")


bot.infinity_polling()

        



















""")

