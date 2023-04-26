from configparser import ConfigParser


class AppConfig:
    def __init__(self):
        config = ConfigParser()
        config.read('cfg/config.ini')

        tg_section = config['Telegram']

        self.tg_api_token = tg_section['ApiToken']
        self.tg_chat_id = tg_section['ChatId']
