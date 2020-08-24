"""
Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        def helper(node, is_left):
            if not node: return
            nonlocal total
            
            if is_left and not node.left and not node.right:
                total += node.val
                
            helper(node.left, True)
            helper(node.right, False)
            
        helper(root, False)
        return total
