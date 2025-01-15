from datetime import datetime
import pytz

# Создаем объект datetime для Лос-Анджелеса
la_timezone = pytz.timezone('America/Los_Angeles')
la_time = la_timezone.localize(datetime(2023, 12, 25, 15, 0, 0))


# Список временных зон для конвертации
timezones = {
    'Москва': 'Europe/Moscow',
    'Нью-Дели': 'Asia/Kolkata',
    'Сидней': 'Australia/Sydney',
    'Рио-де-Жанейро': 'America/Sao_Paulo',
    'Кейптаун': 'Africa/Johannesburg'
}

# Конвертируем и выводим время для каждой временной зоны
for zone,zone_val in timezones.items():
    cur_tz = pytz.timezone(zone_val)
    cur_t = la_time.astimezone(cur_tz)
    event_time = la_time.astimezone(cur_tz)
    print(f"Webinar place - {zone}.Webinar time - {event_time}")