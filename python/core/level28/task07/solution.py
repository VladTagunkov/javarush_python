import matplotlib.pyplot as plt

# Данные для круговой диаграммы
fruits = ['Яблоки', 'Бананы', 'Апельсины', 'Груши']
preferences = [30, 25, 20, 25]

# Построение круговой диаграммы
plt.pie(preferences,labels=fruits)

# Добавление заголовка
plt.title('Предпочтения фруктов')

# Отображение диаграммы
plt.show()