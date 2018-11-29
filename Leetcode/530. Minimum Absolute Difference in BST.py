#530. Minimum Absolute Difference in BST
"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []
        
        self.getMinDiffHelper(root, vals)
        
        minVal = vals[1] - vals[0]
        
        for i in range(2,len(vals)):
            temp = vals[i] - vals[i-1]
            if temp < minVal:
                minVal = temp
                
        return minVal
          
    def getMinDiffHelper(self, root, vals):
        
        if root == None:
            return
        
        self.getMinDiffHelper(root.left, vals)
        vals.append(root.val)
        self.getMinDiffHelper(root.right, vals)
        
