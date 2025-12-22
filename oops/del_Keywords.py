# delete keywords : used to delete object properties or object itself 

# del s1.name 
# del s1

class Student:
    def __init__(self, name):
        self.name = name

# del s1 # deletes the object s1 entirely
s1 = Student("Harshi")        
print(s1.name)
del s1.name
print(s1.name)  #AttributeError: 'Student' object has no attribute 'name'