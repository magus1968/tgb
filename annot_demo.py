def say_something(number: int, word: str) -> list:

    word = word.capitalize()
    return word * number

print(say_something(2, "test"))
