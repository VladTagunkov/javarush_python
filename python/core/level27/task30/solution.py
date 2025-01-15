from datetime import datetime
import pytz

# Запрашиваем у пользователя исходное время и временную зону
original_time_str = input("Введите время в формате 'YYYY-MM-DD HH:MM:SS': ")
original_zone_str = input("Введите исходную временную зону (например, Europe/Moscow): ")
target_zone_str = input("Введите целевую временную зону (например, Europe/Paris): ")

# Парсим введенное время
par_time = datetime.strptime(original_time_str,'%Y-%m-%d %H:%M:%S')

# Получаем временную зону с помощью pytz
zone = pytz.timezone(original_zone_str)

# Привязка времени к временной зоне
t1 = par_time.astimezone(zone)

# Конвертация времени в UTC
t_utc = t1.astimezone(pytz.utc)

# Конвертация времени в целевую временную зону
t2 = t_utc.astimezone(pytz.timezone(target_zone_str))
