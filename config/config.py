from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    bot: TgBot
    
def load_config(path: str | None = None):
    env = Env()
    env.read_env()
    token = env("TOKEN")
    return Config(
        bot=TgBot(token=token)
    )