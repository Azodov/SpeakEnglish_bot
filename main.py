import logging
from oxfordLookup import getDefinitions
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
translator = Translator()

API_TOKEN = '2134514498:AAHEgKNZRCLmJEyUSQ3VzPtrmWu9VNt_qpc'

#configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatche
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Siz so'ragan mavzudagi maqola va malumotlarni sizga qaytarib jo'nataman")


@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)