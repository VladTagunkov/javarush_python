# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

# Напишите тут ваш код
bk1 = {"name":"Cats","author":"Tolstoy","year":2020,'title':"One Two"} 

if "author" in bk1:
    print("Key exist")
else:
    print("Key not exists") 
    
if bk1.get("publisher") is None:
    print("Key not in dict")
else:
    print("Key in dict")
    
        
#if 'title' in bk1.keys():  
if "title" in bk1.keys():
    print("Ключ 'title' присутствует в словаре.")
else:
    print("Ключ 'title' отсутствует в словаре.")
    