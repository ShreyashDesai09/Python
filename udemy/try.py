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

# arr = [1,2,3,4,5,6,7]
# print(arr)
# for i in arr:
#     j = len(arr)
#     for j in range (len(arr),i):
#         print("i",i)
#         print("j",j)
#     print("------------")


# dashes = 0
# a = [1,1,2,2,3,3,2,3,4,6,9,10]
# print(f"ENTERED NUMBERS ARE :- {a}")
# for i in a:
#     key = i
#     count = -1
#     j = i + 1
#     for j in a:
#         if key == j:
#             count = count + 1
#             a.remove(i)
#         if count > -1:
#             print(a)
#             dashes = dashes + count
    
# print(len(a))

# for i in a:
#     if dashes >= 0:
#         a.append(0)
#         dashes = dashes -1


# print(f"{a}")



# a = [1,2,3,3,2]
# b = []
# d = 0

# for i in a:
#     key = i
#     j = i+1
#     count = 0
#     for j in a:
#         if j == key:
#             b.append(i)
#             a.remove(j)
#         count = +1
#     d = d + count    

# print(a)
# print(b)
# print(d)
# print(count)


for i in range(1,7):
    for j in range (1 , i):
        space = j - 7
        for s in space:
            print(f"{j} \t", end= " ")        
    print()
    

    