from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6301830254:AAE_pcjQUizSpOm7fJ21UHxroUgBWKxcOLg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Knopka ustiga bosing', web_app=WebAppInfo(url='https://bestburgerandijon.netlify.app/')))
    await message.answer('Buyurtma berish uchun tanlang', reply_markup=markup)


@dp.message_handler()
async def help(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Knopka ustiga basing', web_app=WebAppInfo(url='https://bestburgerandijon.netlify.app/')))
    await message.answer('Offline holat un', reply_markup=markup)




executor.start_polling(dp)
