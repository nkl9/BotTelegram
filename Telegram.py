import telebot
from telebot import types

bot = telebot.TeleBot('877686854:AAGR_kcDf70arRSR0wzWi4K_8HDumhv9HpM')


@bot.message_handler(commands=['n'])

def start (message):
    bot.send_message(message.from_user.id, "Введите число")
    bot.register_next_step_handler(message, number_to_words)


def number_to_words(message):
    try:
        num = int(message.text)
    except :
        bot.send_message(message.from_user.id, "Введите число")
    f = {1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
    l = {10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок',
    50 : 'пятьдесят', 60 : 'шестьдесят', 70 : 'семьдесят',
    80 : 'восемьдесят', 90 : 'девяносто'}
    s = {11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать',
    14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать',
    17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}
    n1 = num % 10
    n2 = num - n1
    if (num < 10):
        bot.send_message(message.from_user.id, f.get(num))
    elif 10 < num < 20 :
        bot.send_message(message.from_user.id, s.get(num))
    elif num >= 10 and num in l:
        bot.send_message(message.from_user.id, l.get(num))
    elif (num > 20):
        bot.send_message(message.from_user.id, l.get(n2) + ' ' + f.get(n1))
    else:
        bot.send_message(message.from_user.id,'Введено число, которое не лежит в [1:99]!')
@bot.message_handler(content_types=['text'])

def set_message(message):
    bot.reply_to(message,"Введите комаду /n")

bot.polling(none_stop=True, interval=0)
