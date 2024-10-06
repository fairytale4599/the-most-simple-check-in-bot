import telebot
from config import token
import datetime
import threading
import time

bot = telebot.TeleBot(token)
users = []
specific_time = datetime.time(15, 55)

def ifTime() -> bool:
    current_time = datetime.datetime.now().time()
    return current_time.hour == specific_time.hour and current_time.minute == specific_time.minute

def check_time():
    while True:
        if ifTime():
            sendMessage()
        time.sleep(30)

@bot.message_handler(func=lambda m: True)
def fetchId(message):
    msgid = message.chat.id
    if msgid not in users:
        users.append(msgid)
    print(users)

def sendMessage():
    for user_id in users:
        bot.send_message(user_id, "It's 15:55!")

if __name__ == '__main__':
    time_thread = threading.Thread(target=check_time)
    time_thread.start()
    bot.polling(none_stop=True, interval=0)
