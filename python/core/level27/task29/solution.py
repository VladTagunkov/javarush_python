from datetime import datetime
import pytz

# Определяем временные зоны
time_zones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo'
}

# Получаем и выводим текущее время для каждой временной зоны
for zone,zone_val in time_zones.items():
    cur_tz = pytz.timezone(zone_val)
    cur_t = datetime.now().astimezone(cur_tz)
    print(f"{zone} - time is - {cur_t}")