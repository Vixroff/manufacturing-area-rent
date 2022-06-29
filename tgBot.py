import telebot
from config import Config


message_bot = telebot.TeleBot(Config.TGBOT_TOKEN)
chat_id = Config.TGBOT_CHAT_ID   
    