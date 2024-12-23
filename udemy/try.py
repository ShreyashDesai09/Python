# a = [2,2,3,4,5]
# print(len(a))
# x = int(input("SEARCH:"))
# if x <= len(a):
#     print(a[x]) 
# else: 
#     print("ERROR")
    

# name = "asdd,asdwer,awfrh,xerg"
# x = ""
# end = []
# c_count = 0
# comma = name.count(",")
# for i in name:
#     if i != ",":
#         name = name + i
#     elif i == ",":
#         c_count = +1
#         end.append(name)
#     elif c_count == comma:
#         break
# print(comma)
# print(end[0:1])

# name = 'SHREYASH'
# print(name)
# print(len(name))
# x = len(name)-1
# print(x)

# print(name[1:x])

# def remove_char(s):
#     x = len(s)-1
#     print(s[1:x])
        
# name = input("ENTER NAME TO BE SPLITTED:")
# remove_char(name)

arr = [1,2,3,4,5,6,7]
print(arr)
for i in arr:
    j = len(arr)
    for j in range (len(arr),i):
        print("i",i)
        print("j",j)
    print("------------")