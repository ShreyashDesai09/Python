class Room:
    Name = ""
    Hall = "BIG"   #Data Members
    Area = 12
    Wall = 4
    Windows = 2
    Door = 1

    def __init__(self,Name,Wall):   #Constructor
        asd = input("ASD")
        self.Name = Name
        print(f"----------\n{Name}")
        self.Wall = Wall
        print(f"----------\nThere are {Wall} Walls")

    def all(self):   #Member Function
        print("----------\n1. Hall \n2. Area \n3. Wall\n4. Windows\n5. Door")
        s = int(input("ADD WHAT YOU WANT:"))
        # print(f"{s}")
        if s == 1:
            print("ANS",self.Hall)
        elif s == 2:
            print("ANS",self.Area)
        elif s == 3:
            print("ANS",self.Wall)
        elif s == 4:
            print("ANS",self.Windows)
        elif s == 5:
            print("ANS",self.Door)
        else:
            print("ERROR")

D = Room("SHREYASH",66)
D.all()



