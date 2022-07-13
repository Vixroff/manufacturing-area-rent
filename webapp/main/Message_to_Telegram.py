import os

from dotenv import load_dotenv

import requests


load_dotenv()
token = os.getenv('TGBOT_TOKEN')
chat_id = os.getenv('TGBOT_CHAT_ID')


def send_message_to_telegram(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    response = requests.get(url)
    return response.json
