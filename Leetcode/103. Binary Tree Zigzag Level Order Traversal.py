"""
103. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        zigzag = []
        queue = [root]
        traversals = 0
        while queue:
            layer_size = len(queue)
            layer = []
            for i in range(layer_size):
                front = queue.pop()
                if front:
                    layer.append(front.val)
                    queue.insert(0, front.left)
                    queue.insert(0, front.right)
            if traversals % 2 != 0:
                layer.reverse()
            traversals += 1
            if layer:
                zigzag.append(layer)
        
        return zigzag
