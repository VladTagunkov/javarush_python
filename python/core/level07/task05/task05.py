# Ищем ключи.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания). Программа должна:
# Вывести все ключи словаря с использованием метода keys().
# Итерировать по всем ключам и вывести их на экран.

# Напишите тут ваш код
book = {"name":"Capitan", "author":"Flint",'year':1977}

print(book.keys())

for key in book.keys():
    print(key)