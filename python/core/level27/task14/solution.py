from datetime import datetime, timedelta

# Получаем текущую дату
td = datetime.now()

# Принимаем дату от пользователя в формате "YYYY-MM-DD"
user_date = datetime.strptime(input(),'%Y-%m-%d')

# Преобразуем введенную строку в объект даты


# Вычисляем разницу между целевой датой и текущей датой
delta = user_date - td

# Выводим количество оставшихся дней
print(delta.days)