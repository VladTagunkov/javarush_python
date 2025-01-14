# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код

class BankAccount:
    def __init__(self,account_number,initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance
        
    def deposit(self,amount):
        self.initial_balance += amount
    
    def withdraw(self,amount):
        if self.initial_balance < amount:
            print('Not enough money.')
        else:
            self.initial_balance -= amount
        
        
acc = BankAccount(124,100) 
acc.deposit(20)
acc.withdraw(10) 
