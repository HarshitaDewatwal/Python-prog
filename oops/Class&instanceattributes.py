# Class.attributes vs Instance.attributes in Python
class Dog:
    # Class Attribute
    species = "Canis familiaris"  # This attribute is shared by all instances of the class

    def __init__(self, name, age):
        # (object)Instance Attributes
        self.name = name  # This attribute is unique to each instance
        self.age = age    # This attribute is unique to each instance
dog1 = Dog("Buddy", 3)
print(dog1.name)  

print(Dog.species)

# always prefer instance attributes over class attributes if both are present with the same name, obj atrri >> class attri.
