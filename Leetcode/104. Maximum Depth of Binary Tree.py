# 104. Maximum Depth of Binary Tree
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findMaxDepth(root)
    
    def findMaxDepth(self, root):
        if root == None:
            return 0
        
        leftDepth = self.findMaxDepth(root.left) + 1
        rightDepth = self.findMaxDepth(root.right) + 1
        
        return max(rightDepth,leftDepth)
        
