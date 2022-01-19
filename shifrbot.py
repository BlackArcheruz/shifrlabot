import hashlib
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5099410025:AAGwyS_RxRPRHzS22fiygDq7fPBAc-kUlZY'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu alaykum men shifrlash botiman menga parolingizni jo'nating men uni shifrlab jo'nataman")




@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    text = message.text
    shifred_text = hashlib.md5(text.encode('utf-8')).hexdigest()
    await message.answer(shifred_text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)