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
        order = {v:i for i, v in enumerate(inorder)}
        return self.helper(preorder, 0, inorder, 0, len(inorder)-1, order)

    def helper(self, preorder, pre_start, inorder, in_start, in_end, order):
        if in_start > in_end:
            return None
        if in_start == in_end:
            return TreeNode(inorder[in_start])
        root_val = preorder[pre_start]
        in_order_idx = order[root_val]
        root = TreeNode(root_val)
        left_count = in_order_idx - in_start
        right_count = in_end - in_order_idx
        root.left = self.helper(preorder, pre_start+1, inorder, in_start, in_order_idx-1, order)
        root.right = self.helper(preorder, pre_start+left_count+1, inorder, in_order_idx+1, in_end, order)
        return root
