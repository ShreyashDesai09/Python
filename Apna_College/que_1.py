# CREATE A STUDENT AND GIVE AVERAGE OF MARKS

class Student:

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print(f"STUDENT: {self.name}, MARKS: {sum/3}")

    # def __str__(self):
        # return str(f"STUDENT: {self.name}, MARKS: {sum/3}")
     
s1 = Student("Shreyash" , [99,98,97])

print(s1.average())


