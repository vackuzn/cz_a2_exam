import requests
from appconfig import AppConfig


def send_tg_msg(message: str):
    cfg = AppConfig()

    api_token = cfg.tg_api_token
    chat_id = cfg.tg_chat_id
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
