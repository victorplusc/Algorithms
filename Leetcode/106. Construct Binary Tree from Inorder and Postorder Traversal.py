"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            idx = idx_map[val]
            root.right = helper(idx+1, right)
            root.left = helper(left, idx-1)
            return root
        
        idx_map = {val:i for i, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)
