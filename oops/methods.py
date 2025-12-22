# methods are functions that are associated with object instances.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def Welcome(self):
        print("Welcome student, ", self.name)

    def get_marks(self):  # method to return marks , in class the function is called method
        return self.marks

s1 = Student("Harshi", 95)
s1.Welcome()            
print(s1.get_marks())

# create student class that takes name & marks of 3 students as argumnets in constructor. Then create a method to print the average.

class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        def get_avg(self):
            sum = 0
            for val in self.marks:
                sum += val
            print("Hi!", self.name, "Your avg marks is : ", sum/3)
    
s1 = Student("ronak", [95, 80, 90])
s1.get_avg()

s1.name = "kuki"
s1.get_avg()
# def average_marks():
#     total = s1.marks + s2.marks + s3.marks
#     average = total / 3
#     return average        