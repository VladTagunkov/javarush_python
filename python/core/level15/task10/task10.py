# Преобразуем число в десятичное
# Напишите программу, которая принимает двоичное целое число от пользователя,
# преобразует его в десятичное представление и показывает, как оно будет храниться в памяти.
# В программе также должно быть отображено количество байтов, занимаемое числом.
# Напишите тут ваш код

user_num = input()
res = int(user_num, 2)
print(res)
print((res.bit_length()+7)//8)

