# Номер кортежа

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя индекс элемента и вывести значение элемента по этому индексу.
# Если индекс выходит за пределы кортежа, программа должна вывести соответствующее сообщение.

# Напишите тут ваш код
k=[]

for _ in range(5):
    k.append(input())
    
ind = int(input())
k1 = tuple(k)

if len(k1) <= ind:
    print('Ошибка индекса.')
else:
    print(k1[ind])
