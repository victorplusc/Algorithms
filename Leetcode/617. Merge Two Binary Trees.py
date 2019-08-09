"""
617. Merge Two Binary Trees
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time complexity: O(M), where M is the total number of nodes of the full tree
# Space complexity: O(M), where M is the height is the tallest tree, O(M) when it is skewed, in the average case, it will be O(log M)

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.merge_helper(t1, t2)
    
    def merge_helper(self, t1, t2):
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.merge_helper(t1.left, t2.left)
            node.right = self.merge_helper(t1.right, t2.right)
            return node
        elif t1:
            return t1
        else:
            return t2
