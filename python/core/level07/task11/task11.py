# Индексация студентов.

# Напишите программу, которая создает словарь с информацией о студенте (имя, возраст, университет).
# Программа должна:
# Перебирать пары ключ-значение словаря с использованием функции enumerate().
# Вывести индекс, ключ и значение каждой пары.

# Напишите тут ваш код
stud={"name":"Alex","age":22,"university":"MIT"}

for i,(key,value) in enumerate(stud.items()):
    print(f"{i} - {key} + {value}")