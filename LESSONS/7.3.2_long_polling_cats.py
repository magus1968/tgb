#тестируем бота с отправкой кошаков по long polling:

import requests
import time
import os
from environs import Env

API_URL: str = 'https://api.telegram.org/bot'
env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')
API_CATS_URL: str = 'https://aws.random.cat/meow'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('


offset: int = -2
counter: int = 0
chat_id: int
msg: str
cat_response: requests.Response
cat_link: str
timeout: int = 60
updates: dict


def do_something() -> None:
    print('Был апдейт')
    if 'message' in result:
        chat_id = result['message']['from']['id']
        msg = result['message']['text']
    else:
        chat_id = result['edited_message']['from']['id']
        msg = result['edited_message']['text']
    print('updates =', updates)
    print('текст сообщения = ', msg)
    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()['file']
        requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
    else:
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')