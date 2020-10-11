# 938. Range Sum of BST
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        
        total = 0
        if root.val > L:
            total += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            total += self.rangeSumBST(root.right, L, R)
        if L <= root.val <= R:
            total += root.val
        
        return total
