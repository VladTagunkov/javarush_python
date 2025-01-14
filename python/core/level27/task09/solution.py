import datetime

# Получение текущей даты и времени
nd = datetime.datetime.now()

# Форматирование даты и времени
frm = nd.strftime("%d.%m.%Y %H:%M:%S")

# Вывод результата на экран
print(frm)