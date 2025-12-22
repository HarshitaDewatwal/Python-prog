# private attributes and methods: Attributes and methods that are intended to be inaccessible from outside the class.
# In Python, private attributes and methods are defined by prefixing their names with double underscores (__).
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

        def reset_pass(self):
            print(self.__acc_pass)

acc1 = Account("1234567890", "mypassword")
# print(acc1.__acc_pass)  # This will raise an AttributeError
print(acc1.acc_no)  # This will work
print(acc1.reset_pass()) # This will work


# Example

class Person:
    __name = "John Doe"

    def __hello(self):
        print("Hello person!")
    def welcome(self):
        self.__hello()

p1 = Person()

# print(p1.__name)  # This will raise an AttributeError
print(p1.welcome())  # This will work