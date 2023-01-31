import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)

dp = Dispatcher(bot)

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_log.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S',
)


def calc_sum():
    n1, n2 = get_numbers()
    logging.info(f'{n1} + {n2} = {n1 + n2}')
    result = f'{n1} + {n2} = {n1 + n2}'
    return result


def calc_subtraction():
    n1, n2 = get_numbers()
    logging.info(f'{n1} - {n2} = {n1 - n2}')
    result = f'{n1} - {n2} = {n1 - n2}'
    return result


def calc_multiplication():
    n1, n2 = get_numbers()
    logging.info(f'{n1} * {n2} = {n1 * n2}')
    result = f'{n1} * {n2} = {n1 * n2}'
    return result


def calc_division():
    n1, n2 = get_numbers()
    if n2 == 0:
        logging.error('Error. Division by 0')
        result = 'Error. It cannot be divided by 0.'
    else:
        logging.info(f'{n1} / {n2} = {n1 / n2}')
        result = f'{n1} / {n2} = {n1 / n2}'
    return result


def calc_exponentiation():
    n1, n2 = get_numbers()
    logging.info(f'{n1} ** {n2} = {n1 ** n2}')
    result = f'{n1}^{n2} = {n1 ** n2}'
    return result


def calc_root():
    n1, n2 = get_numbers()
    if n2 == 0:
        logging.error('Error. Invalid argument for finding root')
        result = 'Error. Invalid argument for finding root.'
    elif n2 % 2 == 0 and n1 < 0:
        logging.error('Error. Invalid argument for finding root')
        result = 'Error. Invalid argument for finding root.'
    else:
        logging.info(f'{n1} root {n2} = {n1 ** (1 / n2)}')
        result = f'The root of degree {n2} of {n1} is {n1 ** (1 / n2)}'
    return result


def calc_remainde_of_division():
    n1, n2 = get_numbers()
    if n2 == 0:
        logging.error('Error. Division by 0')
        result = "Error. It cannot be divided by 0."
    else:
        logging.info(f'{n1} % {n2} = {n1 % n2}')
        result = f'The remainder of dividing {n1} by {n2} is {n1 % n2}'
    return result


def calc_integer_division():
    n1, n2 = get_numbers()
    if n2 == 0:
        logging.error('Error. Division by 0')
        result = "Error. It cannot be divided by 0."
    else:
        logging.info(f'{n1} // {n2} = {n1 // n2}')
        result = f'Result of integer division {n1} by {n2} is {n1 // n2}'
    return result


@dp.message_handler(Command("start"))
async def select_operation(message: Message):
    await message.answer(text="Hello! I'm andy_bot.\n"
                              "I can help you with some simple math operations, such as:\n"
                              "1 - sum,\n"
                              "2 - subtraction,\n"
                              "3 - multiplication,\n"
                              "4 - division,\n"
                              "5 - exponentiation,\n"
                              "6 - root of first number (second number - degree of root),\n"
                              "7 - remainder of division,\n"
                              "8 - integer division\n"
                              "What type of operation would you prefer?")


@dp.message_handler(Text(equals=["1", "2", "3", "4", "5", "6", "7", "8"]))
async def calculate(message: Message):
    if message.text == "1":
        calc_sum()
    elif message.text == "2":
        calc_subtraction()
    elif message.text == "3":
        calc_multiplication()
    elif message.text == "4":
        calc_division()
    elif message.text == "5":
        calc_exponentiation()
    elif message.text == "6":
        calc_root()
    elif message.text == "7":
        calc_remainde_of_division()
    elif message.text == "8":
        calc_integer_division()

@dp.message_handler()
async def get_numbers(message: Message):
    while True:
        value1 = await message.answer(text='Enter first rational number')
        value2 = await message.answer(text='Enter first rational number')
        try:
            num_1 = float(value1.replace(',', '.'))
            num_2 = float(value2.replace(',', '.'))
            return num_1, num_2
        except:
            await message.answer(text='Error. Incorrect input.')
            return


@dp.message_handler()
async def echo(message: Message):
    logging.error('Incorrect input')
    await message.answer(f'{message.from_user.first_name},'
                         f' please, enter the correct message')


executor.start_polling(dp)