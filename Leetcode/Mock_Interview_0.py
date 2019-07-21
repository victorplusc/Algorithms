"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        visits = []
        self.in_order_traversal(root, visits)
        for i in range(len(visits)-1):
            if visits[i] > visits[i+1]:
                return False
        return True
        
    def in_order_traversal(self, root, visits):
        if root:
            self.in_order_traversal(root.left, visits)
            visits.append(root.val)
            self.in_order_traversal(root.right, visits)
