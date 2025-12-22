# inheritance : when one class acquires the properties of another class
# parent/base class : the class being inherited from
# child/derived class : the class that inherits from another class
 
class Animal:          # parent class
    def speak(self):
        return "Animal speaks"

class Dog(Animal):    # child class
    def bark(self):
        return "Woof!"
dog1 = Dog()
print(dog1.speak())  # inherited method from Animal class   
print(dog1.bark())   # method from Dog class

# types of inheritance :
# 1. single inheritance : when a child class inherits from a single parent class
# 2. multi-level inheritance : when a class is derived from a class which is also derived from another class
# e.g.
class Puppy(Dog):   # grandchild class
    def __init__(self, type):
        self.type = type
puppy1 = Puppy("Bulldog")
print(puppy1.speak())  # inherited from Animal class     


# 3. multiple inheritance : when a class is derived from more than one base class
# e.g.
class Cat:
    def meow(self):
        return "Meow!"
class HybridAnimal(Dog, Cat):  # child class inheriting from Dog and Cat
    def info(self):
        return "I am a hybrid animal."

hybrid1 = HybridAnimal()
print(hybrid1.bark())  # inherited from Dog class
print(hybrid1.meow())  # inherited from Cat class
print(hybrid1.info())  # method from HybridAnimal class


# 4. hierarchical inheritance : when multiple child classes inherit from a single parent class
# 5. hybrid inheritance : a combination of two or more types of inheritance
