from config import Config

import requests


def send_message_to_telegram(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    response = requests.get(url)
    return response.json


if __name__ == "__main__":
    send_message_to_telegram(Config.TGBOT_TOKEN, Config.CHAT_ID, 'message')
