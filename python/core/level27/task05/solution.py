from datetime import datetime

# Получаем текущую дату и время
dt = datetime.now()

# Форматируем дату и время в соответствии с заданным форматом
print(f"{datetime.now():%Y-%m-%d %H:%M:%S}")

# Выводим отформатированную дату и время на экран
