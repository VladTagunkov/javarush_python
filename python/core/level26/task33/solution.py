import time

# Начало измерения времени
time_start = time.time()

# Инициализация суммы
total_sum = 0

# Цикл от 1 до 1000000
for number in range(1, 1000001):
    # Проверяем, является ли число четным
    if number % 2 == 0:
        total_sum += number

# Завершение измерения времени
time_end = time.time()

# Рассчитываем общее время выполнения
execution_time = time_end - time_start

# Вывод общего времени выполнения в секундах
print(f"Общее время выполнения: {execution_time:.6f} секунд")
