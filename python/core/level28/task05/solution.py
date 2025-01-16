import matplotlib.pyplot as plt
import numpy as np

# Создание данных для графика
x = np.arange(0, 11)  # массив x со значениями от 0 до 10
y = x ** 2  # массив y, равный x в квадрате

# Построение линейного графика
plt.plot(x,y)

# Подпись осей и заголовка графика
plt.title("Квадратичная зависимость")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображение графика
plt.show()