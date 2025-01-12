# Нашли кота

# Напишите функцию create_cat_profile(name, age, breed="Неизвестно"), которая принимает имя, возраст и необязательный параметр "порода" (по умолчанию "Неизвестно").
# Функция должна выводить профиль кота в формате "Имя: [name], Возраст: [age], Порода: [breed]".
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

# Напишите тут ваш код

def create_cat_profile(name, age, breed="Неизвестно"):
    profile = f"Имя: {name}, Возраст: {age}, Порода: {breed}"
    print(profile)
    return profile
    
    
create_cat_profile("Sam", 5, breed="Неизвестно")
create_cat_profile("Ram", 1)
create_cat_profile("Mam", 3, breed="Siami")