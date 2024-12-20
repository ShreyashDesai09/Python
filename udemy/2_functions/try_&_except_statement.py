print("How mant 200+ Rohit Sharma scored:")
e = int(input())
try:
    if e == 3:
        print("CORRECT")
    else:
        print("WRONG")
except ValueError:
    print("ENTER ONLY INT")