import threading
from aiogram import Bot, Dispatcher, types
import sqlite3
import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer

API_TOKEN = '8718005981:AAEyYFOywodN1892xFjVKmZWxpchsuN7wmI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ...existing code for database and handlers...

async def main():
    await dp.start_polling(bot)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def run_health_server():
    server = HTTPServer(('0.0.0.0', 8000), HealthHandler)
    server.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=run_health_server, daemon=True).start()
    asyncio.run(main())
