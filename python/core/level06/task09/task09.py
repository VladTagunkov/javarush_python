# Котовасия

# Напиши программу, которая хранит множество из 5 самых популярных имен котов.
# Пользователь должен пытаться угадать их. Когда он угадывает имя кота, оно удаляется из множества.
# Цель игры - угадать всех котов за как можно меньшее число попыток.

# Напишите тут ваш код
cat_set = {'Bars','Boris','Oris','Mill','Opp'}

cnt = 0
while len(cat_set)!=0:
    name = input()
    if name in cat_set:
        cat_set.discard(name)
        cnt+=1
    else:
        cnt+=1
        
print(cnt)
