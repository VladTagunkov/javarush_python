# Использование Future

# Напишите асинхронную функцию, которая принимает объект Future
# и устанавливает для него результат после задержки в 1 секунду.
# Создайте цикл событий, объект Future и используйте функцию для установки результата.
# Затем выведите результат Future на экран.

# Напишите тут ваш код

async def set_future(fut,value):
    await asyncio.sleep(1)
    fut.set_result(value)
    
async main():
    lp = asyncio.get_running_loop()
    ft = lp.create_future()
    await set_future(ft,'Hi!')
    print(ft.result())
    
asyncio.run(main())