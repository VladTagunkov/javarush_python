# Управление задачами (Tasks)

# Напишите асинхронную программу, которая создает две задачи.
# Первая задача должна ждать 1 секунду и печатать "Первая задача завершена",
# вторая задача должна ждать 2 секунды и печатать "Вторая задача завершена".
# Используйте asyncio.create_task() для создания задач и asyncio.run() для их выполнения.

# Напишите тут ваш код

async def task1():
    await asyncio.sleep(1)
    print("Первая задача завершена")
    
async def task2():
    await asyncio.sleep(2)
    print("Вторая задача завершена")
    
async main():
    task1 = asyncio.create_task(task1())
    task2 = asyncio.create_task(task2())
    await task1 
    await taks2
    
asyncio.run(main())