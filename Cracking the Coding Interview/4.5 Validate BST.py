#4.5 Validate BST
"""
Implement a function to check if a binary tree is a binary search tree.
"""
from math import inf

def validateBST(root):
    stack = []
    lastVal = -inf

    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if stack != []:
                root = stack.pop()
                if lastVal > root.val: return False
                lastVal = root.val
                root = root.right
            else:
                break
            
    return True
