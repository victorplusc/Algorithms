#671. Second Minimum Node In a Binary Tree
"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        nodes = set()
        self.addNodesToSet(root, nodes)
        
        nodes.remove(min(nodes))
        if len(nodes) != 0:
            return min(nodes)
        return -1
        
    
    def addNodesToSet(self, root, nodes):
        if root:
            self.addNodesToSet(root.left, nodes)
            self.addNodesToSet(root.right, nodes)
            nodes.add(root.val)
