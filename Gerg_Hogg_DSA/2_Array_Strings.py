print("-----------------ARRAY-----------------")
a = [1,2,3]
print(a)

#Append - Insert Element at End of Array - O(1)
a.append(4)
print(a)

#Pop - Delete Element at End of Array - O(1)

a.pop()
print(a)

#Insert - Insert at a specific Location O(n)

a.insert(2,8)
print(a)

#Modify an Element - O(1)
a[2] = 33
print(a)

#Accessing a certain locations - O(1)
print(a[2])

#Check if an Element is present in Array - O(n)
if 33 in a:
    print(True)
else:
    print(False)

#Length of Array - O(1)
print(len(a))


#-----------------STRINGS-----------------

print("-----------------STRINGS-----------------")

#Append to end of String - O(n)

s = "hello"
b = s + " world"
print(b)

#Check if something is in String - O(n)
if "h" in s:
    print(True)
else:
    print(False)

#Accessing Position
print(s[2])

#Length of String - O(1)
print(len(s))





