# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.is_unival = True
        self.in_order_traversal(root)
        return self.is_unival
    
    def in_order_traversal(self, root):
        while root:
            if root.val != self.in_order_traversal(root.left) and root.left != None:
                self.is_unival = False
            if root.val != self.in_order_traversal(root.right) and root.right != None:
                self.is_unival = False
            return root.val
