import schedule
import time
import logging

# Настраиваем логирование для записи в консоль
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def reminder():
    # Задача, которая выводит напоминание
    logging.info("Пора сделать недельный план!")

# Настройка расписания на каждое воскресенье в 18:00
schedule.every().sunday.at("18:00").do(reminder)

while True:
    # Проверка расписания
    schedule.run_pending()
    # Задержка в 1 минуту, чтобы избежать излишней загрузки процессора
    time.sleep(1)