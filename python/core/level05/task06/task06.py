# Поиск строки

# Напишите программу, которая создает список из 10 элементов.
# Программа просит пользователя ввести строку, а потом проверяет - есть она в списке или нет.

# Напишите тут ваш код
tmp=['one','tho','theree','four','five','six','seven','eight','nine','ten']
val=input()

if val in tmp:
    print('Element in list')
else:
    print('Element not in list')