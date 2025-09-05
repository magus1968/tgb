import asyncio


async def main():
    print("\nHello World!")


asyncio.run(main())
# Cамую первую корутину, являющуюся точкой входа в программу, добавляют в цикл событий
# c помощью функции run библиотеки asyncio.
# В программе должна быть только одна такая точка входа


# main()    # если просто вызовем main() как для обычных функций, получим:
# RuntimeWarning: coroutine 'main' was never awaited
#  main()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback


# await main()   # ести  добавим await, то получим синтаксическую ошибку
# SyntaxError: 'await' outside function - что мы использовали ключевое слово await вне функции.


# Для корректной работы асинхронных функций - их недостаточно просто вызывать.
# Нужно добавлять их в цикл событий