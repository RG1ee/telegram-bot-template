from aiogram import Dispatcher

from tgbot.handlers.users import register_all_message_handlers
from tgbot.misc.set_default_commands import set_default_commands
from tgbot.handlers.message import register_message_handlers


def register_all_handlers(dp: Dispatcher):
    register_all_message_handlers(dp)
    register_message_handlers(dp)


async def register_all_services(dp: Dispatcher):
    register_all_handlers(dp)
    await set_default_commands(dp)
