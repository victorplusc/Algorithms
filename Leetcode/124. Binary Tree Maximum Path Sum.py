"""
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(log N)
"""
Clarify examples, and path definition. E.g. 
Input: [0,1,2]
       0
      / \
     1   2
Output: 3

Algorithm:
1) Base case:
    for nodes without children, maximum gain is 0 from both branches
2) For every node, we want to only take the left/right branches if we get a net gain. So if they are < 0, just don't explore it (represented by 0)
3) However when we recurse upwards, we cannot just take the maximum of the whole tree, we must at most take one branch
4) So we take the max(node.val+left, node.val+right)
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float('-inf')
        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            curr_max = node.val + left + right
            max_path = max(max_path, curr_max)
            
            return max(node.val+left, node.val+right)
            
        dfs(root)
        return max_path
