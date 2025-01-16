# Выполнение нескольких задач параллельно

# Напишите программу, которая использует asyncio.gather() для выполнения нескольких асинхронных задач параллельно
# и собирает их результаты.

# Напишите тут ваш код

import asyncio

async def fun3():
    await asyncio.sleep(1)
    print("F3 here!")

async def task1():
    print("Hi from f1!")
    await asyncio.sleep(2)
    print("F1 awake!")
    
async def task2():
    print("Hi from f2!")
    await asyncio.sleep(2)
    print("F2 awake!")
    
    
async def main():
    res = await asyncio.gather(task1(),task2())
    print(res)
    
asyncio.run(main())