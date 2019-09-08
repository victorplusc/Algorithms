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

import collections

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        zigzag = []
        deque = collections.deque()
        deque.append(root)
        traversals = 0
        while deque:
            layer_size = len(deque)
            layer = []
            for i in range(layer_size):
                front = deque.pop()
                if front:
                    layer.append(front.val)
                    deque.appendleft(front.left)
                    deque.appendleft(front.right)
            if traversals % 2 != 0:
                layer.reverse()
            traversals += 1
            if layer:
                zigzag.append(layer)
        
        return zigzag
            
        
        
        
        
        
        
        
        
        
        
