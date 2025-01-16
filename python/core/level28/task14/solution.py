import numpy as np
import matplotlib.pyplot as plt

# Генерация 1000 случайных нормальных чисел с средним 50 и стандартным отклонением 10
data = np.random.normal(50, 10, 1000)

# Построение гистограммы
plt.hist(data,bins=20,color='red',edgecolor='black')

# Добавление заголовка
plt.title("Настроенная гистограмма нормального распределения")

# Добавление сетки
plt.grid(True)

# Отображение гистограммы
plt.show()