class Student:

    college = "KIT" # This is class attributed that are common for all instances. Means Same for all
    name = "NOT ENTERED"

    def __init__(self, name, marks):
        self.name = name # This is instance attribute that change according to user i/p
        self.marks = marks
        # print("Adding students to Database")

    # Object Attribute have Higher Priority than Class Attribute

    def __str__(self):
        return str(f"Student Name: {self.name} Marks: {self.marks} College: {self.college} ")
    
    def welcom(self): # Funcitions in Class are Methods
        print("WLECOME",self.name)

s1 = Student("SHREYASH", 99)
s2 = Student("",69)

print(s1)
# print(s2)
print(s1.welcom())