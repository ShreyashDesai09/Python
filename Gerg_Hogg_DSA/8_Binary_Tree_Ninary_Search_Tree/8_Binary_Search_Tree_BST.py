class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
A = TreeNode(5)
B = TreeNode(1)
C = TreeNode(8)
D = TreeNode(-1)
E = TreeNode(3)
F = TreeNode(7)
G = TreeNode(9)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

# print(A)

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

print(in_order(A))

def search_bst(node,target):
    if not node:
        return print(False)
    
    if node.val == target:
        return print(True)
    
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)
    
search_bst(A, 8)