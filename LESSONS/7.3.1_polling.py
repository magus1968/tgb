import requests
import time
import os
from environs import Env

API_URL = 'https://api.telegram.org/bot'
env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')

offset = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:   # Чтобы прервать бесконечный цикл - нажать Ctrl+C
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')