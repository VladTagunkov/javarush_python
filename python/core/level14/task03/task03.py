# Создание и выполнение асинхронных функций

# Напишите программу, которая создает и выполняет несколько асинхронных функций,
# каждая из которых использует оператор await для ожидания завершения другой асинхронной функции.

# Напишите тут ваш код
import asyncio

async def fun3():
    await asyncio.sleep(1)
    print("F3 here!")

async def fun1():
    print("Hi from f1!")
    await fun3()
    print("F1 awake!")
    
async def fun2():
    print("Hi from f2!")
    await fun3()
    print("F2 awake!")
    
    
async def main():
    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())
    
    await task1 
    await task2 
    
    
asyncio.run(main())