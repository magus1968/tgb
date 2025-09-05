import asyncio
import time


async def send_mail(num):
    print('Улетело сообщение {}'.format(num))
    await asyncio.sleep(1)
    print('Сообщение {} доставлено'.format(num))


async def main():
    tasks = [send_mail(i) for i in range(10)]
    await asyncio.gather(*tasks)  # звездочка `*` означает распаковать


start_time = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {time.time() - start_time} с')

# Пример из обучающего видео в Дзене
# async def main()
#     await asyncio.gather(one(), two(), three())  # идентично
# asyncio.create_task(one())
# asyncio.create_task(two())
# await asyncio.create_task(three())