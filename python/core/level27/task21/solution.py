import schedule
import time

def reminder():
    print("Пора проверить почту!")

# Настройка задачи на ежедневное выполнение в 10:00
schedule.every().day.at("10:00").do(reminder)

# Бесконечный цикл для постоянной работы программы
while True:
    schedule.run_pending()
    time.sleep(1)