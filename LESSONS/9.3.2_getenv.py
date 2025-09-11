import os

# Вариант с Perplexity из урока "7.2.3_api_auto_requests_correct.py":
    # from dotenv import load_dotenv
    # load_dotenv()  # Загружаем токен из .env файла

# Вариант из урока 9.3.2:
import dotenv  # Импортируем библиотеку
dotenv.load_dotenv()  # С помощью функции load.dotenv загружаем переменную из .env в окружение

print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))