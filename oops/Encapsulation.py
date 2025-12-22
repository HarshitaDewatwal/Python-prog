# Encapsulation: Bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class.
# Example: A capsule that contains medicine, the medicine is encapsulated within the capsule.
# In Python, encapsulation is implemented using classes and access modifiers (public, protected, private).
# public: accessible from anywhere
# protected: accessible within the class and its subclasses
# private: accessible only within the class

# data + function = capsule

# class with methods and attributes = object

# wrapping data and methods into a single unit
# example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


