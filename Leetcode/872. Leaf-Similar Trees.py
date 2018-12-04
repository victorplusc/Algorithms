#872. Leaf-Similar Trees
"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.x = []
        self.y = []
        
        self.findLeaves(root1, self.x)
        self.findLeaves(root2, self.y)
        
        return self.x == self.y
        
    
    def findLeaves(self, root, array):
        
        if root:
            if root.left == None and root.right == None:
                array.append(root.val)
            self.findLeaves(root.left, array)
            self.findLeaves(root.right, array)
            
