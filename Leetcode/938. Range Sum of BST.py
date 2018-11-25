# 938. Range Sum of BST
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.sum = 0
        
        def traverse(node):
            if node:
                if L <= node.val <= R:
                    self.sum += node.val
                if node.val > L:
                    traverse(node.left)
                if node.val < R:
                    traverse(node.right)
            
        traverse(root)

        return self.sum
        
