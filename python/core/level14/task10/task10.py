# Запуск и остановка цикла событий

# Напишите программу, которая запускает цикл событий в бесконечном режиме.
# Запланируйте остановку цикла через 3 секунды, используя метод call_later.
# Публикация состояния запущен ли цикл до и после вызова метода stop().

# Напишите тут ваш код
import asyncio 

def cl():
    print('Callback!')
    asyncio.get_event_loop().stop()

lp = asyncio.get_event_loop()
print("cicle run!")
lp.call_later(3,cl)
lp.run_forever()

