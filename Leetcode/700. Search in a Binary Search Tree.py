"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val > val:
                if val < root.val and root.left == None:
                    return None
                return self.searchBST(root.left, val)
            elif root.val < val:
                if val > root.val and root.right == None:
                    return None
                return self.searchBST(root.right, val)
            else:
                return root
                
# Time complexity: O(log N) average case, O(N) worst case
# Space complexity: O(N)
