# Создаем классы.

# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку
# и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг, используя методы объекта.

# Напишите тут ваш код
class Library:
    book=['One','Two','Three','More']
    def add_book(self,new_book):
        return self.book.append(new_book)
        
    def display_books(self):
        print(self.book)
        
lib = Library()
lib.add_book('Four')
lib.add_book('Five')
lib.display_books()