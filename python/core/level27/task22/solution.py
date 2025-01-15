import schedule
import time

# Функция для напоминания о необходимости подготовить отчет
def remind():
    print("Пора подготовить отчет!")

# Настройка расписания задачи на каждый будний день в 8:30 утра
schedule.every().monday.at("08:30").do(remind)
schedule.every().tuesday.at("08:30").do(remind)
schedule.every().wednesday.at("08:30").do(remind)
schedule.every().thursday.at("08:30").do(remind)
schedule.every().friday.at("08:30").do(remind)

# Основной цикл для выполнения задач в соответствии с расписанием
while True:
    schedule.run_pending()
    time.sleep(1)