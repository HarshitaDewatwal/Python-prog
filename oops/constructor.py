# constructor is a special method in Python classes that is automatically called when an object of the class is created.
# It is used to initialize the attributes of the object.
# all classes have a function called _init_() 

class Student:
    # default constructor
    def __init__(self):
        pass

    
    # // parametrized constructor
    def __init__(self, fullname, age, marks):  # fullname or  name
        print("adding new student...")
        self.name = fullname
        self.age = age
        self.marks = marks

s1 = Student("Harshi", 22, 99)
print(s1.name, s1.age, s1.marks)        