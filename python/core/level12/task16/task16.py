# Сериализация с помощью yaml

# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля yaml.
# Объектом для сериализации будет словарь, содержащий информацию о фильме: название, режиссёр и год выпуска.

# Напишите тут ваш код
import yaml

# Пример словаря с информацией о фильме
film_info = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}

ser = yaml.dump(film_info)
res = yaml.load(ser,Loader=yaml.FullLoader)
# # Напишите тут ваш код
# with open("film.yaml","w") as file:
#     yaml.dump(film_info,file)
    
# with open("film.yaml","r") as file:
#     res = yaml.load(file,Loader=yaml.FullLoader)
    
print(res)