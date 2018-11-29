#94. Binary Tree Inorder Traversal
"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        self.inorderHelper(root, vals)
        return vals
    
    def inorderHelper(self, root, vals):
        if root == None:
            return
        self.inorderHelper(root.left, vals)
        vals.append(root.val)
        self.inorderHelper(root.right,vals)
