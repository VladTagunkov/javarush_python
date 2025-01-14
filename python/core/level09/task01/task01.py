# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

# Напишите тут ваш код

class Car:
    make = "Opel"
    model = "Astra"
    year = 1980
    
    def display_info(self):
        print(f"car {self.make} {self.model} {self.year}")
        

car = Car()
car.display_info()

