# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода ключей и значений.

# Напишите тут ваш код
person={"name":"Alex","age":22,"adress":{"city":"Moscow",
                                         "street":"Lenina"
    
                                        },
                                         "info":{"email":"1@2.com",
                                                "tel":555444
                                         }}
 def rec(person_):                                        
     for key,value in person_.items():
         print(f"{key} - {value}")
         if isinstance(value,dict):
                rec(value)
            
rec(person)