# When We Don't Want To Use Self In A Fuction In A Class We Use @staticmethod 
# With Self Written It Becomes Non-Static Method

class Student:

    @staticmethod
    def hello():
        print("HELLO! WORLD")

s1 = Student()
print(s1.hello())
