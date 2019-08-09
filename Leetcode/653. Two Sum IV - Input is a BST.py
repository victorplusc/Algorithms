"""
653. Two Sum IV - Input is a BST
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
"""

## Incomplete!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.in_order_traversal(root, root, k, False)
        
    def in_order_traversal(self, tree, node, k, valid):
        if node:
            self.in_order_traversal(tree, node.left, k, valid)
            res = self.find_complement(tree, node, k-node.val)
            if res: valid = True
            self.in_order_traversal(tree, node.right, k, valid)
            return res or valid
            
    def find_complement(self, tree, current, n):
        if tree:
            if n == tree.val and tree != current:
                return True
            elif tree.right and n > tree.val:
                return self.find_complement(tree.right, current, n)
            elif n < tree.val and tree.left:
                return self.find_complement(tree.left, current, n)
            else:
                return False
            
            
            
