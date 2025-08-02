from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
import os
import secrets
import string
import asyncio

load_dotenv('tokens/BOT_TOKEN.env') # загрузка токена из .env
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def gen_pass_ult(number=12): # генерация модифицированного пароля
    chars = string.ascii_letters + string.digits + '!@#$%^:;&?*()<>'
    password = ''.join(secrets.choice(chars) for i in range(number))
    return password

async def gen_pass(number=12): #
    chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(chars) for i in range(number))
    return password

@dp.message(lambda message: message.text == '/start') # приветствие бота
async def start(message: Message):
    await message.answer('Привет, я бот для создания безопасных паролей. Напиши /gen_pass <number> чтобы сгенерировать обычный пароль без спец. символов или напиши /gen_pass_ult <number> чтобы сгенерировать пароль со спец. символами. По умолчанию пароль генерируется из 12 символов')

@dp.message(lambda message: message.text.startswith('/gen_pass_ult')) # генерация модифицированного пароля
async def gen_pass_ult_func(message: Message):
    parts = message.text.split()

    if len(parts) > 1:
        number = " ".join(parts[1:])

        password = await gen_pass_ult(int(number))
        await message.answer(f'Вот ваш сгенерированный пароль:\n\n{password}')
    else:
        await message.answer(f'Вот ваш сгенерированный из 12 символов (по умолчанию):\n\n{await gen_pass_ult()}')

@dp.message(lambda message: message.text.startswith('/gen_pass')) # генерация обычного пароля
async def gen_pass_func(message: Message):
    parts = message.text.split()

    if len(parts) > 1:
        number = " ".join(parts[1:])

        password = await gen_pass(int(number))
        await message.answer(f'Вот ваш сгенерированный пароль:\n\n{password}')
    else:
        await message.answer(f'Вот ваш сгенерированный из 12 символов (по умолчанию):\n\n{await gen_pass()}')

async def main(): # главный цикл программы
    while True:
        try:
            print('Запуск бота')
            await dp.start_polling(bot)
        except Exception as e:
            print(f'Ошибка {e}')
            print('Перезапуск бота')
            await asyncio.sleep(3)

if __name__ == '__main__':
    asyncio.run(main())