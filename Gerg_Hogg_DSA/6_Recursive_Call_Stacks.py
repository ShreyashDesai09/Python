# Fibonacci
# F(0) = 0
# F(1) = 1
# n > 1 : F(n) = F (n-1) + F (n-2)

# Time: O(2^n), Space: O(n)
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

print(F(5))


#USING LINKED LIST
class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

Head.next = A
A.next = B
B.next = C

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print( ' -> '.join(elements))

display(Head)

# Reverse printing of Node

# Time : O(n), Space: O(n) 

def reverse(node):
    if not node:
        return
    

    reverse(node.next)
    print(node)

reverse(Head)

