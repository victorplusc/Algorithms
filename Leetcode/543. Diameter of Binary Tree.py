"""
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        v = [0]
        self.dfs(root, 1, v)
        return v[0]

    def dfs(self, node, depth, v):
        if not node:
            return 0
        left = self.dfs(node.left, depth + 1, v)
        right = self.dfs(node.right, depth + 1, v)
        v[0] = max(*v, left + right)
        return max(left, right) + 1
