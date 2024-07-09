import telebot
from background import keep_alive
from telebot import types



bot = telebot.TeleBot('7247435233:AAF1D3oNxbIb7qWsFWQYUWiaAbtJuXC6Mzc')
MANAGER_CHAT_ID = 7192518179

user_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Чем я могу вам помочь?")
"""
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Добро пожаловать! Ваш ID: {message.chat.id}")
"""
@bot.message_handler(func=lambda message: True)
def forward_to_manager(message):
     bot.send_message(MANAGER_CHAT_ID, f"Новое сообщение от пользователя @{message.from_user.username} ({message.from_user.id}): {message.text}")
     user_states[MANAGER_CHAT_ID] = message.chat.id
     bot.reply_to(message, "Ваше сообщение было перенаправлено менеджеру. Ожидайте ответа.")



@bot.message_handler(func=lambda message: message.chat.id == MANAGER_CHAT_ID)
def handle_manager_message(message):
    if MANAGER_CHAT_ID in user_states:
        user_id = user_states[MANAGER_CHAT_ID]
        bot.send_message(user_id, f"Сообщение от менеджера: {message.text}")
        bot.reply_to(message, "Ваше сообщение было отправлено пользователю.")
    else:
        bot.reply_to(message, "Нет активного диалога с пользователем.")




keep_alive()
bot.polling(none_stop=True)
