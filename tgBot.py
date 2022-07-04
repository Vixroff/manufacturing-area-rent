from config import Config

import telebot

message_bot = telebot.TeleBot(Config.TGBOT_TOKEN)
chat_id = Config.TGBOT_CHAT_ID
