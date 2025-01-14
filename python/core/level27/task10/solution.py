from datetime import datetime

# Определение текущей даты
tn = datetime.now()

# Форматирование даты в формат "YYYY-MM-DD"
nd1 = tn.strftime("%Y-%m-%d")

# Форматирование даты в формат "DD.MM.YYYY"
nd2 = tn.strftime("%d.%m.%Y")

# Вывод даты на экран
print(nd1)
print(nd2)