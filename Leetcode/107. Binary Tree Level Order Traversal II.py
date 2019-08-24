"""
107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        level_order = []
        
        while queue:
            layer_size = len(queue)
            layer = []
            for i in range(layer_size):
                front = queue.pop()
                if front:
                    layer.append(front.val)
                    queue.insert(0, front.left)
                    queue.insert(0, front.right)
            if layer:
                level_order.append(layer)
        
        level_order.reverse()
        return level_order
