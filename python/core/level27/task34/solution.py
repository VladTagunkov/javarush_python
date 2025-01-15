import schedule
import time

# Функция для напоминания о разминке
def reminder():
    print("Напоминание: пора сделать разминку!")

# Настройка расписания: запуск функции напоминания каждый час
schedule.every().hour.do(reminder)

# Основной цикл для выполнения задач по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
