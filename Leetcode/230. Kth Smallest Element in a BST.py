"""
230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.recursive(root, k)
        return self.iterative(root, k)

    # Time complexity: O(N)
    # Space complexity: O(H)
    def iterative(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
    
    # Time complexity: O(N)
    # Space complexity: O(H)
    def recursive(self, root: TreeNode, k: int) -> int:
        count = n = 0

        def inorder_traversal(node):
            nonlocal count, n 
            if node.left:
                inorder_traversal(node.left)
            count += 1
            if count == k:
                n = node.val
            if node.right:
                inorder_traversal(node.right)
                
        inorder_traversal(root)
        return n
