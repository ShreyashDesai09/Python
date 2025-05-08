#Stack - Last In First Out - LIFO

stk = []
print(stk)

#Append to TOP of Stack - O(1)

stk.append(1)
stk.append(2)
stk.append(3)

print(stk)

#POP from Stack - O(1)

x = stk.pop()

print(x)
print(stk)


#Ask whats on TOP - O(1)

print(stk[-1])

#Ask if something in Stack - O(1)
if stk:
    print(True)

