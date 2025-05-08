#Queue - First In First Out - FIFO 

from collections import deque

q = deque()
print(q)

#Enqueue - Add Element to Right - O(1)

q.append(5)
q.append(6)
q.append(7)
q.append(8)
print(q)

#Dequeue - Remove Elememt from Left - O(1)

q.popleft()
print(q)

#Peek from left side - o(1)
print(q[0])

#Peek from Right Side - O(1)
print(q[-1])