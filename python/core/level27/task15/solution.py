import datetime
import time

while True:
    # Получаем текущее время
    td = datetime.datetime.now()
    # Определяем время для запуска (сегодня в 8:00 утра)
    target = td.replace(hour = 8, minute = 0, second = 0, microsecond = 0)

    # Если текущее время уже после 8:00 утра, запланировать запуск на следующий день
    if td >= target:
        target += datetime.timedelta(days=1)

    # Рассчитываем время ожидания до следующего запуска в секундах
    delta = (target - td).total_seconds()

    # Пауза до следующего запуска
    time.sleep(delta)

    # Вывод сообщения о начале работы
    print("Пора вставать и начинать работу!")
