from aiogram import types, dispatcher


async def start_user(message: types.Message):
    await message.bot.send_message(
        message.chat.id,
        "Hello",
    )


def register_all_message_handlers(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        start_user,
        commands=["start"],
        state="*",
    )
