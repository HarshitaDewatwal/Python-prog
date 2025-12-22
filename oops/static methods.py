# methods that don't use the self parameter (work at the class level)
# are called static methods. They are defined using the @staticmethod decorator.
# decorator is a special type of function that modifies the behavior of another function.

class MathOperations:
    @staticmethod   # decorator to define static method
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# decorators allow you to wrap a function and modify its behavior without changing its code.