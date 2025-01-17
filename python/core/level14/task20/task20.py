# Асинхронное программирование

# Напишите асинхронную программу, которая выполняет 30 задач параллельно.
# Каждая задача должна ожидать 2 секунды и затем выводить своё сообщение "Task n done", где n - номер задачи.
# Используйте модуль asyncio.

# Напишите тут ваш код
import asyncio 

async def task(n):
    await asyncio.sleep(2)
    print(f"Task {n+1} done")
    
    
async def main():
    for i in range(30):
        task = asyncio.create_task(task(i))
        result = await asyncio.gather(tasks)
    
asyncio.run(main())