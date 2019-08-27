"""
1026. Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root:
            return self.ancestor_helper(root, root.val, root.val)
        
    def ancestor_helper(self, root, max_ancestor, min_ancestor):
        if root:
            max_ancestor = max(root.val, max_ancestor)
            min_ancestor = min(root.val, min_ancestor)
            left = self.ancestor_helper(root.left, max_ancestor, min_ancestor) if root.left else -1
            right = self.ancestor_helper(root.right, max_ancestor, min_ancestor) if root.right else -1
            
            return max(max_ancestor-min_ancestor, left, right)
