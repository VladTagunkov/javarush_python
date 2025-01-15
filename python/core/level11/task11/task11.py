# Перегрузка операторов сравнения

# Напишите класс Person, который будет представлять человека с атрибутами name и age.
# Реализуйте перегрузку операторов сравнения == и < для сравнения людей по возрасту.

# Напишите тут ваш код
class Person:
    def __init__(self,name,age):
        self.age = age 
        self.name = name 
        
    def __eq__(self, other):
        if self.age == other.age:
            return True 
        else:
            return False
    
    def __lt__(self, other):
        if self.age < other.age:
            return True 
        else:
            return False