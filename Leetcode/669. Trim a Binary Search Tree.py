"""
669. Trim a Binary Search Tree
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2

Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
 """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        return self.trim(root, L, R)

    def trim(self, node, L, R):
        if not node:
            return None
        elif node.val > R:
            return self.trim(node.left, L, R)
        elif node.val < L:
            return self.trim(node.right, L, R)
        else:
            node.left = self.trim(node.left, L, R)
            node.right = self.trim(node.right, L, R)
            return node
