import datetime
from datetime import timedelta

def parse_time_string(time_str):
    """Парсит строку времени и возвращает часы и минуты как целые числа."""
    try:
        hours, minutes = map(int, time_str.split(':'))
        if not (0 <= hours < 24) or not (0 <= minutes < 60):
            raise ValueError("Некорректное время")
        return hours, minutes
    except ValueError:
        raise ValueError("Некорректный формат времени. Пожалуйста, введите время в формате ЧЧ:ММ.")

def round_minutes_to_nearest_five(minutes):
    """Округляет заданное количество минут до ближайшего кратного 5."""
    remainder = minutes % 5
    if remainder < 2.5:
        return minutes - remainder  # Округление вниз
    else:
        return minutes + (5 - remainder)  # Округление вверх

def round_time_to_nearest_five_minutes(time_str):
    """Округляет переданное время до ближайших 5 минут."""
    # Парсинг строки времени
    # Округление минут
    time_ = datetime.strptime(time_str,"HH:MM")
    hours = time_.hours
    minutes = time_.minutes
    rounded_minutes = round_minutes_to_nearest_five(minutes)
    
    if rounded_minutes % 60 == 0:
        hours += 1
        rounded_minutes=0 

    # Если округленные минуты равны 60, добавляем 1 час и сбрасываем минуты на 0


    # Возвращаем округленное время в формате строки
    return f"{hours:02}:{rounded_minutes:02}"

def get_time_input(prompt):
    """Запрашивает и округляет ввод времени от пользователя."""
    while True:
        try:
            time_str = input(prompt)  # Запрос времени у пользователя
            return round_time_to_nearest_five_minutes(time_str)  # Округление времени
        except ValueError as e:
            print(e)  # Вывод сообщения об ошибке, если формат времени неверен

def main():
    print("Программа для округления времени рабочего графика")
    start_time = get_time_input("Введите время начала (ЧЧ:ММ): ")
    end_time = get_time_input("Введите время окончания (ЧЧ:ММ): ")

    print("Округленное время:")
    print(f"Время начала: {start_time}")
    print(f"Время окончания: {end_time}")

# Запуск основной программы
main()
