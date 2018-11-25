#4.2 Minimal Tree
"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def minBST(array : "List of sorted elements"):
    return generate(array, 0, len(array)-1)

def generate(array, start, end):
    if (end < start):
        return None
    mid = (start + end)//2
    node = TreeNode(array[mid])
    node.left = generate(array, start, mid - 1)
    node.right = generate(array, mid + 1, end)
    return node

def inOrderTraversal(node: "TreeNode"):
    if node != None:
        inOrderTraversal(node.left)
        print(node.val)
        inOrderTraversal(node.right)
