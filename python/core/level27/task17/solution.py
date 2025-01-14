import schedule
import time

def task():
    print("Выполняем задачу")

# Настройка выполнения задачи каждую минуту
schedule.every().minute.do(task)

# Бесконечный цикл для постоянной работы программы
while True:
    schedule.run_pending()
    time.sleep(1)