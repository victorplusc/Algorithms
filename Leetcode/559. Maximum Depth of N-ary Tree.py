"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        
        depths = []
        
        for node in root.children:
            depths.append(self.maxDepth(node) + 1)
        
        if depths == []:
            return 1
        else:
            return max(depths)
