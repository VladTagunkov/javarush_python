# Отрицательные кортежи

# Напишите программу, которая создает кортеж из 7 элементов, запрашиваемых у пользователя.
# Затем программа должна вывести третий с конца и предпоследний элемент кортежа с использованием отрицательных индексов.

# Напишите тут ваш код

elems=[]
for _ in range(7):
    elems.append(input())
    
tup = tuple(elems)
print(tup[-3])
print(tup[-2])