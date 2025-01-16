# Создание и получение цикла событий

# Напишите программу, которая создает новый цикл событий, устанавливает его как текущий и печатает его.
# Затем создайте еще один новый цикл событий и снова установите его как текущий.
# Убедитесь, что вы правильно меняете циклы событий.

# Напишите тут ваш код
import asyncio 

nl1 = asyncio.new_event_loop()
asyncio.set_event_loop(nl1)
print(asyncio.get_event_loop())

nl2 = asyncio.new_event_loop()
asyncio.set_event_loop(nl2)
print(asyncio.get_event_loop())