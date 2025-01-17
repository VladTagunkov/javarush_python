import matplotlib.pyplot as plt
import numpy as np

# Создание данных
x = np.linspace(0, 10, 100)
y = x**2

plt.figure(figsize=(8,6))
# Построение графика
plt.plot(x,y)
plt.xlim(0,10)

# Сохранение графика в PDF с прозрачным фоном
plt.savefig("quadratic_graph.pdf",transparent=True)