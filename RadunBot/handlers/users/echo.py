from loader import dp
from aiogram import types


@dp.message_handler(text='/start')
async def bot_echo(message: types.Message, state):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)
    await message.answer(text)
    await message.reply(text)





@dp.message_handler()
async def bot_echo(message: types.Message, state):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)
    await message.answer(text)
    await message.reply(text)
