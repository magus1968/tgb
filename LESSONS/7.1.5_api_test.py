import requests  # noqa: F401

api_url = 'http://numbersapi.com/43'

response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)  # При другом коде ответа выводим этот код


# Любопытные решения из комментариев.
# ! Выполняются командой `Run Python File in Terminal:` т.к. имеется ввод данных от пользователя

# import requests
# api_url = 'http://numbersapi.com/'
# number = input('number: ')
# print(requests.get(api_url + number).text)

# import requests
# api_url = 'http://numbersapi.com/'
# number = input('введите число ')
# response = requests.get(api_url + number)
# print(response.text)