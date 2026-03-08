# بوت المستخدم البسيط
# هذا الملف يتم تشغيله لكل بوت مستخدم
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = sys.argv[1]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply('بوتك يعمل بنجاح!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
