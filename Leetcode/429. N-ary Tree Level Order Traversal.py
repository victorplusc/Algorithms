"""
429. N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# Time complexity: O(N)
# Space complexity: O(k), k being the size of the largest layer
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        levels = []
        q = collections.deque()
        q.append(root)
        while q:
            current = []
            for i in range(len(q)):
                front = q.pop()
                if not front: continue
                current.append(front.val)
                for child in front.children:
                    q.appendleft(child)
            if current:
                levels.append(current)
        return levels
