# إدارة وتشغيل بوتات المستخدمين
import subprocess
import threading
import time

bots_processes = {}

def start_bot(bot_id, token):
    # شغل بوت المستخدم في عملية منفصلة
    proc = subprocess.Popen(['python', 'user_bot.py', token])
    bots_processes[bot_id] = proc
    return proc

def stop_bot(bot_id):
    proc = bots_processes.get(bot_id)
    if proc:
        proc.terminate()
        del bots_processes[bot_id]

# يمكن إضافة وظائف إعادة التشغيل والمراقبة لاحقاً
