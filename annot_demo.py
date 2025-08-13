def say_something(number: int, word: str) -> str:

    word = word.capitalize()
    return word * number

print(say_something(2, "test"))
