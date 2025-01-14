import schedule
import time

def job():
    print("Прошел час")

# Настройка задачи на выполнение каждый час
schedule.every(1).hour.do(job)

# Бесконечный цикл для постоянной работы программы
while True:
    schedule.run_pending()
    time.sleep(1)