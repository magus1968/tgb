from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str

def get_user_info(user: User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'

user_1 = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info(user_1))

 
@dataclass
class Book:
    title: str
    author: str

book = Book(title="Fahrenheit 451", author="Bradbury")
book
# Book(title='Fahrenheit 451', author='Bradbury')
book.author
# 'Bradbury'



@dataclass
class Person:
     first_name: str = "Ahmed"
     last_name: str = "Besbes"
     age: int = 30
     job: str = "Data Scientist"

ahmed = Person()
print(ahmed)
# Person(first_name='Ahmed', last_name='Besbes', age=30, job='Data Scientist')


from dataclasses import astuple, asdict  # noqa: E402

print(astuple(ahmed))
# ('Ahmed', 'Besbes', 30, 'Data Scientist')

print(asdict(ahmed))
# {'first_name': 'Ahmed',
# 'last_name': 'Besbes',
# 'age': 30,
# 'job': 'Data Scientist'}


# Где объекты хранят аннотации типов: атрибут __annotations__

def get_string(string: str, number: int) -> str:
    return string * number

print(get_string.__annotations__)
# {'string': <class 'str'>, 'number': <class 'int'>, 'return': <class 'str'>}



# Вот так, например, можно оформить класс Config, в экземпляре которого будут храниться
# конфигурационные данные для наших с вами ботов и данные для подключения к базе данных,
# которые мы будем получать сначала из переменных окружения:

from dataclasses import dataclass  # noqa: E402


@dataclass
class DatabaseConfig:
    host: str  # URL-адрес базы данных
    user: str  # Username пользователя базы данных
    password: str  # Пароль к базе данных
    database: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    bot: TgBot
    db: DatabaseConfig


# Если создать экземпляр класса Config:

# config = Config(
#    bot=TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS),  # noqa: F821
#    db=DatabaseConfig(
#        host=DB_HOST,  # noqa: F821
#        user=DB_USER,  # noqa: F821
#        password=DB_PASSWORD,  # noqa: F821
#        database=DATABASE  # noqa: F821
#    )
# )

# То, например, получить токен бота можно, будет так:
# token = config.bot.token

# А пароль к базе данных так:
# db_password = config.db.password