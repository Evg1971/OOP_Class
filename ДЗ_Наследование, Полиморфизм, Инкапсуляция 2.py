class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__balance += value
        else:
            print("Только числовые значения допустимы для пополнения счета")

    def withdraw(self, value):
        if isinstance(value, (int, float)) and value > 0:
            if value <= self.__balance:
                self.__balance -= value
            else:
                print("Недостаточно средств на счете")
        else:
            print("Только числовые значения допустимы для снятия со счета")


Evg = BankAccount(100)
print(f"Ваш баланс: {Evg.get_balance()}")

Evg.deposit(50)
print(f"Баланс после пополнения: {Evg.get_balance()}")

Evg.withdraw(88)
print(f"Баланс после снятия: {Evg.get_balance()}")

Evg.deposit('100')
Evg.withdraw(1000)


