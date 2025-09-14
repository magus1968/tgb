import requests
import pprint
import time
import os
from environs import Env


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str

while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    pprint.pprint(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1


# attempt = 29
# {'ok': True, 'result': []}
# attempt = 30
# {'ok': True,
# 'result': [{'message': {'chat': {'first_name': 'Алексей',
#                                  'id': 565210636,
#                                  'last_name': 'Смирнов',
#                                  'type': 'private',
#                                  'username': 'mr_magus'},
#                         'date': 1757857857,
#                         'from': {'first_name': 'Алексей',
#                                  'id': 565210636,
#                                  'is_bot': False,
#                                  'is_premium': True,
#                                  'language_code': 'ru',
#                                  'last_name': 'Смирнов',
#                                  'username': 'mr_magus'},
#                         'message_id': 42,
#                         'text': 'Что ж. Урок 7.2.6 работает :)'},
#             'update_id': 393039995}]}