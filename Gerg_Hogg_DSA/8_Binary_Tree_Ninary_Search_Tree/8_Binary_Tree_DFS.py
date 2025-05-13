''' 1] Depth First Search
        1) Pre order Traversal  - Node Left Right
        2) In Order Traversal   - Left Node Right
        3) Posr Orver Traversal - Left Right Node
'''

# Binary Tree

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    

#           1
#       2       3  
#     4   5  10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

# Recursive Pre Order Transversal (DFS) Time: O(n) Space: O(n)

def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

print("\n----------Pre Order----------\n")
print(pre_order(A))

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

print("\n----------In Order----------\n")
print(in_order(A))

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

print("\n----------Post Order----------\n")
print(post_order(A))

# Check if Value Exists (DFS) Time: O(n), Space:O(n)
def search(node,target):
    if not node:
        return False

    if node.val == target:
         return True
    
    return search(node.left, target) or search(node.right, target)

print("\n-----FINDING NODE IN TREE-----\n")
print(search(A, 2))
