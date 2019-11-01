"""
590. N-ary Tree Postorder Traversal
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:
       1
  3    2     4
5   6
Return its postorder traversal as: [5,6,3,2,4,1].
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        path = []
        stack = [root]
        while stack:
            if root and root.children:
                for child in root.children:
                    stack.append(child)
            if root:
                path.append(root.val)
            root = stack.pop()
        
        return path[::-1]
