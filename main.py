import telebot
from telebot import types
from os import getenv
from sys import exit
import logger as lg

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = telebot.TeleBot(token=bot_token)

ask_user = "OK, please, enter two rational numbers\n" \
           "(use space for splitting entering numbers,\n" \
           "e.g. for input 3 and 4.5 enter '3 4.5'"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm andy_bot.\n"
                                      "I can help you with some simple math /operation")


@bot.message_handler(commands=['operation'])
def operation(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Sum')
    button2 = types.KeyboardButton('Subtraction')
    button3 = types.KeyboardButton('Multiplication')
    button4 = types.KeyboardButton('Division')
    button5 = types.KeyboardButton('Exponentiation')
    button6 = types.KeyboardButton('Finding root')
    button7 = types.KeyboardButton('Remainder of division')
    button8 = types.KeyboardButton('Integer division')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    bot.send_message(message.chat.id, 'Select operation', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def select_operation(message):
    global ask_user
    if message.text == "Sum":
        bot.send_message(message.chat.id, ask_user)
        bot.register_next_step_handler(message, calc_sum)
    elif message.text == "Subtraction":
        bot.register_next_step_handler(message, calc_subtraction)
    elif message.text == "Multiplication":
        bot.register_next_step_handler(message, calc_multiplication)
    elif message.text == "Division":
        bot.register_next_step_handler(message, calc_division)
    elif message.text == "Exponentiation":
        bot.register_next_step_handler(message, calc_exponentiation)
    elif message.text == "Finding root":
        bot.register_next_step_handler(message, calc_root)
    elif message.text == "Remainder of division":
        bot.register_next_step_handler(message, calc_remainde_of_division)
    elif message.text == "Integer division":
        bot.register_next_step_handler(message, calc_integer_division)
    else:
        bot.send_message(message.chat.id, 'Please, click button')
        operation(message)


def calc_sum(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        lg.logging.info(f'{n1} + {n2} = {n1 + n2}')
        result = f'{n1} + {n2} = {n1 + n2}'
        bot.send_message(message.chat.id, f"Done!\n{result}")
        operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_subtraction(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        lg.logging.info(f'{n1} - {n2} = {n1 - n2}')
        result = f'{n1} - {n2} = {n1 - n2}'
        bot.send_message(message.chat.id, f"Done!\n{result}")
        operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_multiplication(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        lg.logging.info(f'{n1} * {n2} = {n1 * n2}')
        result = f'{n1} * {n2} = {n1 * n2}'
        bot.send_message(message.chat.id, f"Done!\n{result}")
        operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_division(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        if n2 == 0:
            lg.logging.error('Error. Division by 0')
            result = 'Error. It cannot be divided by 0.'
            bot.send_message(message.chat.id, f"{result}")
            operation(message)
        else:
            lg.logging.info(f'{n1} / {n2} = {n1 / n2}')
            result = f'{n1} / {n2} = {n1 / n2}'
            bot.send_message(message.chat.id, f"Done!\n{result}")
            operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_exponentiation(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        lg.logging.info(f'{n1} ** {n2} = {n1 ** n2}')
        result = f'{n1}^{n2} = {n1 ** n2}'
        bot.send_message(message.chat.id, f"Done!\n{result}")
        operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_root(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        if n2 == 0:
            lg.logging.error('Error. Invalid argument for finding root')
            result = 'Error. Invalid argument for finding root.'
            bot.send_message(message.chat.id, f'{result}')
            operation(message)
        elif n2 % 2 == 0 and n1 < 0:
            lg.logging.error('Error. Invalid argument for finding root')
            result = 'Error. Invalid argument for finding root.'
            bot.send_message(message.chat.id, f'{result}')
            operation(message)
        else:
            lg.logging.info(f'{n1} root {n2} = {n1 ** (1 / n2)}')
            result = f'The root of degree {n2} of {n1} is {n1 ** (1 / n2)}'
            bot.send_message(message.chat.id, f"Done!\n{result}")
            operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_remainde_of_division(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        if n2 == 0:
            lg.logging.error('Error. Division by 0')
            result = "Error. It cannot be divided by 0."
            bot.send_message(message.chat.id, f'{result}')
            operation(message)
        else:
            lg.logging.info(f'{n1} % {n2} = {n1 % n2}')
            result = f'The remainder of dividing {n1} by {n2} is {n1 % n2}'
            bot.send_message(message.chat.id, f"Done!\n{result}")
            operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


def calc_integer_division(message):
    value = message.text
    print(value)
    value1 = value.split()[0]
    value2 = value.split()[1]
    try:
        n1 = float(value1.replace(',', '.'))
        n2 = float(value2.replace(',', '.'))
        if n2 == 0:
            lg.logging.error('Error. Division by 0')
            result = "Error. It cannot be divided by 0."
            bot.send_message(message.chat.id, f'{result}')
            operation(message)
        else:
            lg.logging.info(f'{n1} // {n2} = {n1 // n2}')
            result = f'Result of integer division {n1} by {n2} is {n1 // n2}'
            bot.send_message(message.chat.id, f"Done!\n{result}")
            operation(message)
    except:
        lg.logging.error("Error")
        result = 'Error. Incorrect input'
        bot.send_message(message.chat.id, f'{result}')
        operation(message)


bot.infinity_polling()
