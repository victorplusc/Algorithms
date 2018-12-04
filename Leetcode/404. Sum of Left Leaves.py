#404. Sum of Left Leaves
"""
Find the sum of all left leaves in a given binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, False)
    
    def helper(self, root, isLeft):
        sum = 0
        if root:
            if isLeft and root.left == None and root.right == None:
                sum += root.val
            sum += self.helper(root.left, True)
            sum += self.helper(root.right, False)
            
        return sum
