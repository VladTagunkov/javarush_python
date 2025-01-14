from datetime import datetime

# Запрос ввода первой даты
first_date = datetime.strptime(input(),'%Y-%m-%d')
# Запрос ввода второй даты
second_date = datetime.strptime(input(),'%Y-%m-%d')

# Преобразование строк в объекты datetime


# Вычисление разницы между датами
delta = second_date - first_date

# Вывод количества дней
print(delta.days)