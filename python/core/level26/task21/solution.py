import logging

# Настройка логирования
logging.basicConfig(filename='program_log.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Запись сообщений в лог-файл
logging.info("Программа запущена")
logging.info("Выполняется процесс")
logging.info("Программа завершена")