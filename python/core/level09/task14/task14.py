# Автопарк.

# Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# Используйте функцию issubclass() для выполнения проверки.
# Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.

# Напишите тут ваш к
def check_subclass(var,check_cl):
    if issubclass(var,check_cl):
        return True
    else:
        return False 
        
class Vehicle:
    pass 

class Car(Vehicle):
    pass 

class Bicycle(Vehicle):
    pass


print(check_subclass(Car,Vehicle))
print(check_subclass(Bicycle,Vehicle))