#Collection of same data types

#LIST
# print("--------LIST-----------")
# get = int(input("ENTER LIST NO. YOU WANT TO ENTER: "))
# l = []
# for i in range(0,get):
#     a = input(f"{i} = ")
#     l.append(a)

# print(l)

#ADDING LIST IN LIST

# print("\nNOW LETS ENTER DIFF DATA TYPES IN ONE LIST")
# print("--------ADDING LIST IN LIST-----------")
# get2 = int(input("\nENTER HOW MANY LISTS IN LIST YOU NEED: "))
# l2 = []
# l3 = []
# for i in range (0,get2):
#     get3 = int(input(f"\n{i} LIST LENGTH:"))
#     # typee = input("ENTER TYPE OF LIST: ") 
#     for j in range (0,get3):
#         # val = input()
#         # if val == typee:
#         get4 = input()
#         l3.append(get4)
#     l2.append(l3) 
        
# print(l2)

#DELETING LIST
# print("--------DELETING ITEM OF LIST-----------")
# spam = [1,2,3,4,5,6]
# print(spam)
# delete = int(input("DELETE:"))
# del spam [delete]
# print(spam)

a = ["1","2","3","4"]
for i in range(len(a)):
    print(str(i) + a[i])