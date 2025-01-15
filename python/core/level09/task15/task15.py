# Базовые классы.

# Создайте два базовых класса Base1 и Base2, каждый из которых имеет метод describe().
# Создайте производный класс Combined, который наследует от обоих базовых классов.
# Реализуйте метод describe() в каждом базовом классе. Вызовите метод describe() у объекта класса Combined.

# Напишите тут ваш код

class Base1:
    def describe(self):
        print("Base1")
        super().describe()

class Base2:
    def describe(self):
        print("Base2")
    
class Combined(Base1,Base2):
    def describe(self):
        super().describe()
        

c1 = Combined()

c1.describe()