    #        OOPS 
    # 1. Abstraction
    # 2. Encapsulation
    # 3. Inheritance
    # 4. Polymorphism

# Abstraction: Hiding the complex implementation details and showing only the necessary parts to the user.
# Example: You drive a car, you just need to know how to drive (steering, accelerator, brake) without knowing the internal working of the car engine.
# abstraction in OOPs is achieved using classes and objects.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True   # unnecessary details hidden from user
        self.brk = False
        self.clutch = False
        print("Car started")
car1 = Car()
car1.start()        # output : Car started





#    // practice question
# Create Account class with 2 attributes - balance and account no. Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

        # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Your current balance is: Rs.", self.balance)

        # credit method
        def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("Your current balance is: Rs.", self.balance)
        # balance method
        def get_balance(self):
            return self.balance


acc1 = Account(10000, "1234567890")        
acc1.debit(1000)
acc1.credit(500)    

# output : Rs. 1000 was debited
# Your current balance is: Rs. 9000
# Rs. 500 was credited
# Your current balance is: Rs. 9500

