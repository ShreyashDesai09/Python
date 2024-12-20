name = input("ENTER NAME:")

if name:
    print(f"HELLO {name}")
else:
    print(f"Not Hello")

o = 1
while o < 3:
    print(f"Current Count: {o}")
    o = o + 1 
    print(f"Next is {o}")

find = ""
alert = 3
while find != "SHREYASH":
    find = input("ENTER NAME TO BE FOUND:")
    if find == "SHREYASH" or find == "shreyash" :
        print("CORRECT")
        break
    else:
        print("WRONG TRY AGAIN!!!")
        alert = alert - 1
        if alert != 0:
            print(f"LAST {alert} Chances Remaining")
        else:
            print("OUT OF CHANCES")
            break

# i = 1
for i in range(1,5):
    print(i)