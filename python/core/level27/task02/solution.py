from datetime import datetime
from datetime import date

# Создаем объект datetime для текущей даты и времени
td = datetime.today().date()

# Указываем дату рождения
bd = date(1980,5,15)

# Рассчитываем разницу между текущей датой и датой рождения
difference = td - bd

# Выводим количество дней между датами
print(f"Количество дней между текущей датой и датой рождения: {difference.days}")