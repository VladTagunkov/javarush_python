# Первый на выход

# Напишите программу, которая создает список из 5 элементов, запрашивает у пользователя элемент для удаления
# и удаляет первый найденный элемент из списка с использованием метода remove().
# Программа должна вывести обновленный список.

# Напишите тут ваш код
ls = [1,2,3,40,5]
elem = int(input())
ls.remove(elem)
print(ls)