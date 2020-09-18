"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left=0, right=len(inorder)):
            nonlocal pre_idx
            if left == right:
                return None
            
            val = preorder[pre_idx]
            root = TreeNode(val)
            
            idx = idx_map[val]
            pre_idx += 1
            root.left = helper(left, idx)
            root.right = helper(idx+1, right)
            return root

        pre_idx = 0
        idx_map = {val: i for i, val in enumerate(inorder)}
        return helper()
