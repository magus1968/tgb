import requests
import time
import os
import pprint
from dotenv import load_dotenv

API_URL = 'https://api.telegram.org/bot'

load_dotenv()  # Загружаем токен из .env файла
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Используем токен из .env файла

TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 50

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    # print(updates)  # Добавил из коммента, чтобы нагляднее стал работать процесс запросов в терминале
    pprint.pprint(updates) # Или ещё нагляднее import pprint | pprint.pprint(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1