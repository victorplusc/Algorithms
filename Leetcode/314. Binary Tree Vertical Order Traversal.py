"""
314. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]
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
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        d = {}
        self.vertical_helper(root, 0, d)
        output = []
        for i in sorted([_ for _ in d]):
            output.append(d[i])
        return output
    
    def vertical_helper(self, root, position, d):
        if root:
            self.vertical_helper(root.left, position-1, d)
            if position in d:
                d[position].append(root.val)
            else:
                d[position] = [root.val]
            self.vertical_helper(root.right, position+1, d)
