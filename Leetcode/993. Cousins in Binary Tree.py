"""
993. Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        node_x = None
        node_y = None
        queue = [[None, root]]
        layer = 0
        while queue:
            layer += 1
            layer_size = len(queue)
            for i in range(layer_size):
                front = queue.pop(0)
                if not front[1]:
                    continue
                if front[1].val == x:
                    node_x = [front[0], layer]
                elif front[1].val == y:
                    node_y = [front[0], layer]
                if node_x and node_y:
                    if node_x[0]==node_y[0] or node_x[1] != node_y[1]:
                        return False
                    return True
                queue.append([front[1], front[1].left])
                queue.append([front[1], front[1].right])
        return False
