import matplotlib.pyplot as plt

# Данные о доле пользователей различных операционных систем
labels = ['Windows', 'macOS', 'Linux', 'Other']
sizes = [45, 30, 15, 10]  # Произвольные значения долей
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Уникальные цвета для каждой категории

# Вычисляем наибольшую долю для выделения сектора
explode = [0.1, 0, 0, 0]

# Создание круговой диаграммы
plt.pie(sizes,labels=labels,explode=explode,colors=colors,autopct='%1.1f%%')

# Устанавливаем равные оси для обеспечения круговой формы
plt.axis('equal')

# Отображение диаграммы на экране
plt.show()