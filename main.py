from aiogram import Bot, Dispatcher
from config.config import load_config
from handlers.user_handlers import rt

config = load_config()
token = config.bot.token

bot = Bot(token)
dp = Dispatcher()

dp.include_router(rt)

if __name__ == "__main__":
    dp.run_polling(bot)