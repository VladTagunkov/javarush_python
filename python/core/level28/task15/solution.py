import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
uniform_data = np.random.uniform(0, 100, 500)
normal_data = np.random.normal(50, 5, 500)

# Построение гистограмм
plt.hist(uniform_data,bins=15,alpha=0.6,label='Uniform Data')
plt.hist(normal_data,bins=15,alpha=0.6,label='Normal Data')

# Настройка графика
plt.grid(True)
plt.legend()
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.title("Сравнение двух распределений")

# Отображение графика
plt.show()