a = 10 #Global Scobe [can be accessed everywhere]

def num():
    z = 20 #Local Scope [Cannot be used outside function]
    #There fore z cannot be printed 
    print(a)

num()
print(z)