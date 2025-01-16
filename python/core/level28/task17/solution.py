import matplotlib.pyplot as plt

# Процентные значения для каждой категории
percentages = [30, 25, 20, 25]
categories = ["Пицца", "Бургер", "Суши", "Паста"]

# Создание круговой диаграммы
plt.pie(percentages,labels=categories,autopct='%1.1f%')

# Убедимся, что круг имеет круглую форму
plt.axis('equal')

# Отображение диаграммы
plt.show()