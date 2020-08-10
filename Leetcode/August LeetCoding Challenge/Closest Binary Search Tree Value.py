"""
Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.iterative_search(root, target)
    
    # Time complexity: O(H)
    # Space complexity: O(H)
    def search_bst(self, root, target, curr=float('inf')):
        if not root:
            return curr
        if abs(curr-target) > abs(root.val-target):
            curr = root.val
        if target < root.val:
            curr = self.search_bst(root.left, target, curr)
        elif target > root.val:
            curr = self.search_bst(root.right, target, curr)
        return curr
    
    # Time complexity: O(H)
    # Space complexity: O(1)
    def iterative_search(self, root, target):
        min_diff = float('inf')
        min_v = None
        while root:
            curr = abs(root.val - target)
            if min(min_diff, curr) != min_diff:
                min_v = root.val
                min_diff = curr
            root = root.left if target < root.val else root.right
        
        return min_v
