# بوت الاستضافة الرئيسي
# يستخدم aiogram

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 # لم يعد هناك executor في aiogram v3
import sqlite3

API_TOKEN = '8718005981:AAEyYFOywodN1892xFjVKmZWxpchsuN7wmI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# قاعدة بيانات بسيطة
conn = sqlite3.connect('bot_host.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS bots (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, token TEXT, status TEXT)''')
conn.commit()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or ''
    c.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    await message.reply('مرحباً بك في منصة استضافة بوتات تيليجرام! أرسل /add لإضافة بوت جديد.')

@dp.message_handler(commands=['add'])
async def add_handler(message: types.Message):
    await message.reply('أرسل توكن البوت الذي تريد استضافته:')

@dp.message_handler(lambda m: len(m.text) == 46 and m.text.startswith('5'))
async def token_handler(message: types.Message):
    user_id = message.from_user.id
    token = message.text.strip()
    # تحقق من صحة التوكن (مبدئي)
    c.execute('INSERT INTO bots (user_id, token, status) VALUES (?, ?, ?)', (user_id, token, 'stopped'))
    conn.commit()
    await message.reply('تم حفظ التوكن! يمكنك الآن إدارة البوت من لوحة التحكم.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
