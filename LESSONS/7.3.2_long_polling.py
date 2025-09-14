import requests
import time
import pprint
import os
from environs import Env

API_URL = 'https://api.telegram.org/bot'
env = Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')

offset = -2
timeout = 60
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True: 
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    pprint.pprint(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')