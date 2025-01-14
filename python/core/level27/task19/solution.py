import schedule
import time

# Функция, которая будет выполняться утром
def good_morning():
    print("Доброе утро")

# Функция для проверки системы
def system_check():
    print("Проверка системы")

# Настройка расписания задач
schedule.every(1).day.at("08:00").do(good_morning)
schedule.every().monday.at("15:00").do(system_check)
schedule.every().wednesday.at("15:00").do(system_check)

# Основной цикл для выполнения задач в соответствии с расписанием
while True:
    schedule.run_pending()
    time.sleep(1)
