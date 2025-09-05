def say_something(number: int, word: str) -> str:

    word = word.capitalize()
    return word * number

print(say_something(2, "test"))

# Ниже будет несколько примеров для закрепления темы "Аннотации типов"

def some_function(number: int | float) -> None:
    pass

def another_some_function(number: int | float | complex = 0) -> None:
    pass

def get_tuple(lst: list[float | bool]) -> tuple[int, ...]:
    return tuple(int(num) for num in lst)
print(get_tuple([1.0, False, 2.3]))

def do_something(arg: dict[int, str | bool]) -> None:
    pass

from typing import Literal  # noqa: E402
user: dict[Literal['name'] | Literal['second_name'] | Literal['username'], str] = {}
user['name'] = 'John'
