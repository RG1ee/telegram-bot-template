from aiogram import types, dispatcher


# Эхо функция
async def echo_message(message: types.Message):
    await message.bot.send_message(
        message.chat.id,
        message.text,
    )


# Регистрация всех message хэндлеров
def register_message_handlers(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        echo_message,
        content_types=types.ContentTypes.TEXT,
    )
