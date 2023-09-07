import asyncio

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentTypes
from aiogram.utils.executor import start_webhook

TOKEN = '6593693542:AAHZNVVPju5nesUbB6HnL0RJoflI-HKx5qM'
WEBHOOK_HOST = '79da-178-218-201-17.ngrok.io'  # Domain name or IP address which your bot is located.
WEBHOOK_PORT = 443  # Telegram Bot API allows only for usage next ports: 443, 80, 88 or 8443
WEBHOOK_URL_PATH = '/foziljon'  # Part of URL
WEBHOOK_URL = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_URL_PATH}"
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001


BAD_CONTENT = ContentTypes.PHOTO & ContentTypes.DOCUMENT & ContentTypes.STICKER & ContentTypes.AUDIO

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def salom_(message:types.Message):
    await message.answer("Salom")


async def on_startup(app):
    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        if not webhook.url:
            await bot.delete_webhook()

        await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(app):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
