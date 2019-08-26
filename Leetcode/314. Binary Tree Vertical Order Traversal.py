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
        self.bfs(root, d)
        return [d[i] for i in sorted(d)]
    
    def bfs(self, root, d):
        queue = [(root, 0)]
        position = 0
        while queue:
            front, position = queue.pop()
            if front:
                queue.insert(0, (front.left, position-1))
                queue.insert(0, (front.right, position+1))
                if position in d:
                    d[position].append(front.val)
                else:
                    d[position] = [front.val]
