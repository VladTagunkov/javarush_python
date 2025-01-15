from datetime import datetime, timedelta

# Функция для округления времени до ближайшего 15-минутного интервала
def round_time_to_nearest_minute(dt):
    discard = timedelta(minutes = dt.minute % 15,
                        seconds = dt.second,
                        microseconds = dt.microsecond)
    dt -= discard
    if discard >= timedelta(minutes=15/2):
        dt += timedelta(minutes=15)
    return dt


# Тестируем функцию с текущим временем
current_time = datetime.now()
rounded_time = round_time_to_nearest_minute(current_time)
print("Текущее время:", current_time)
print("Округленное время:", rounded_time)
