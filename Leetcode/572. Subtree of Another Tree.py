"""
572. Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time complexity: O(N*M)
# Space complexity: O(N), max recursion in s
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)
    
    def equals(self, x, y):
        if not (x and y):
            return x is y
        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)
    
    def traverse(self, s, t):
        if not s:
            return False
        return self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t)
        
