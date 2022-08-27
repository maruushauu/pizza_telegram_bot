from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()



TOKEN = "5673977970:AAHEkGRGNI-A8KGWWcR4NX_Sn6cZKNGIbj4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


