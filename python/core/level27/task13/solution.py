from datetime import datetime, timedelta

# Создание объекта datetime для текущей даты и времени
td = datetime.now()

# Создание timedelta для добавления 7 дней
nd = timedelta(days = 7)

# Добавление 7 дней к текущей дате и времени
new_date = td + nd

# Вывод обоих объектов datetime
print(td)
print(new_date)