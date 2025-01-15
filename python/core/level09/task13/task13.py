# Домашние животные.

# Напишите функцию check_type для проверки, является ли переданный объект экземпляром класса Animal или его подклассов.
# Используйте функцию isinstance() для выполнения проверки.
# Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов.

# Напишите тут ваш код

def check_type(check_class,my_class):
    if isinstance(check_class,my_class):
        return True
    else:
        return False
        
class Animal:
    def sound(self):
        return 'MMMM!!'
        
class Dog(Animal):
    def sound(self):
        return super().sound()+' Wofff!'
    
class Cat(Animal):
    def sound(self):
        return super().sound()+' Miau!'
        
cat = Cat()
dog = Dog()

print(check_type(cat,Animal))
print(check_type(dog,Animal))