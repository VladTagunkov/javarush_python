import matplotlib.pyplot as plt
import random

# Генерация случайных чисел
random_numbers = [random.randint(1, 100) for _ in range(1000)]

# Построение гистограммы
plt.hist(random_numbers,bins=10)

# Настройка заголовка и осей
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title("Распределение случайных чисел")

# Отображение гистограммы
plt.show()