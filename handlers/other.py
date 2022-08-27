from aiogram import types, Dispatcher
import json
import string
from create_bot import dp


#@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)






#    if message.text == 'Привет':
#        await message.answer('И тебе привет')
        # ставим условие проверки,если боту написать привет,то он будет отвечать и тебе привет


#    await message.answer(message.text)      # бот будет эхом отвечать на наши сообщения
#    await message.reply(message.text)       # упоминает автора сообщения и отвечает ему
#    await bot.send_message(message.from_user.id, message.text)  # отправляет сообщение в личку
