from tgbot.settings import consts
from tgbot.settings.data import Config, TgBot


def load_config() -> Config:
    return Config(
        tg_bot=TgBot(
            token=consts.TOKEN,
        )
    )
