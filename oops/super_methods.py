# super() method: is used to call a method from a parent class.
# It is commonly used in inheritance to access methods from a base class.
# super() allows you to call a method from the parent class without explicitly naming it.
# This is especially useful in multiple inheritance scenarios.
# Example:
class Vehicle:
    def start_engine(self):
        return "Engine started"
class Car(Vehicle):
    def start_engine(self):
        parent_message = super().start_engine()  # calling method from parent class
        return parent_message + " in Car"   
car1 = Car()
print(car1.start_engine())  # Output: Engine started in Car
    