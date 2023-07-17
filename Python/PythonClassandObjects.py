# class Person:
#   name = "Amira"
#   occupation = "Software Developer"
#   networth = 100000
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()



# class Details:
#     name = "Rohan"
#     age = 20
# obj1 = Details()
# print(obj1.name)
# print(obj1.age)


# class Car:
#     make = "Land Rover"
#     model = "Defender"
#     colour = "Matt Black"
# obj2 = Car()
# print(obj2.make)
# print(obj2.model)
# print(obj2.colour)

class Student():
    def __init__(self,name,gender,student_ID,subject):
        self.name = name
        self.gender = gender
        self.student_ID = student_ID
        self.subject = subject
    def show_details(self):
        print(f"Student Name: {self.name}, Gender: {self.gender}")
        print(f"Student ID: {self.student_ID} - Student Subject: {self.subject}")


Jay = Student("Jay","Male","172839","Software Engineering")

Jay.show_details()





 
