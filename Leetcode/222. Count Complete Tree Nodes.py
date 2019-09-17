"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time complexity : O(d**2), or O(log**2 N)
# Space complexity: O(1)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        d = self.compute_depth(root)
        if d == 0: return 1
        
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left+(right-left)//2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2**d - 1) + left
    
    def exists(self, curr_pivot, d, node):
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left)//2
            print(pivot, curr_pivot)
            if curr_pivot <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
    
    def compute_depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d
