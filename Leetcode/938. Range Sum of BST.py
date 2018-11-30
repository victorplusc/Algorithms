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

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
    
        return self.helper(root, L, R)
    
    def helper(self, root, L, R):
        sum = 0
        
        if root == None:
            return 0
        
        if L <= root.val <= R:
            sum += root.val
        if L < root.val:
            sum += self.helper(root.left, L, R)
        if R > root.val:
            sum += self.helper(root.right, L, R)
        
        return sum
