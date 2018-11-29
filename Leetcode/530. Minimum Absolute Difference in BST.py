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
        print(vals)
        
        prevVal = vals.pop()
        currVal = vals.pop()
        minVal = abs(currVal - prevVal)
        
        for i in range(len(vals)):
            prevVal = currVal
            currVal = vals.pop()
            temp = abs(currVal - prevVal)
            if temp < minVal:
                minVal = temp
                
        return minVal
        
        
    def getMinDiffHelper(self, root, vals):
        
        if root == None:
            return 0
        
        self.getMinDiffHelper(root.left, vals)
        vals.append(root.val)
        self.getMinDiffHelper(root.right, vals)
        
