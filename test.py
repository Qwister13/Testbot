# -*- coding: utf8 -*-
import pyowm
import telebot
import sys
from importlib import reload
reload(sys)
PYTHONIOENCODING = "UTF-8"

owm = pyowm.OWM('c3138e726cbedcf205ccb822a5a01a1a', language='ru')
bot = telebot.TeleBot("1137506870:AAFxK0M1mmbJnFAGC8qvPwnu0ZRgSIJmIgA")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + \
        "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас холодрыга, одевайся теплее!!!"
    elif temp < 20:
        answer += "Сейчас холодновато, оденься потеплее."
    elif temp < 25:
        answer += "Тепловато!"
    else:
        answer += "ЖАРА!!!!"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
