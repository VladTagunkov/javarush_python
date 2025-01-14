from datetime import datetime

def log_event(event_description, log_file):
    # Получаем текущее время и форматируем его
    tn = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    # Формируем строку логирования
    log_str = f"{tn} {event_description}\n"

    # Открываем файл логов в режиме добавления и записываем событие
    with open(log_file,'a') as file:
        file.write(log_str)


log_file = "events.log"
# Пример записи нескольких событий
events = ["Событие 1", "Событие 2", "Событие 3"]

for event in events:
    log_event(event, log_file)
