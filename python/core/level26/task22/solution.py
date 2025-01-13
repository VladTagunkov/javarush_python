import datetime

# Запрашиваем у пользователя ввод чисел для деления
x = float(input("Введите делимое: "))
y = float(input("Введите делитель: "))

# Пытаемся выполнить деление и обрабатываем ошибку деления на ноль
try:
    result = x / y
    print(f"Результат деления: {result}")

# Логируем ошибку в файл, если произошло деление на ноль
except ZeroDivisionError as e:
    # Открываем файл для записи ошибки
    with open("error_log.txt", "a") as log_file:
        # Получаем текущее время и форматируем его
        current_time = datetime.datetime.now()
        # Записываем ошибку в лог-файл
        log_file.write(f'We have error {e} at {current_time}')
    print("Ошибка: Деление на ноль невозможно. Подробности записаны в error_log.txt.")
