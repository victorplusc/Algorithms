"""
Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        traversal = []
        while q:
            size = len(q)
            level = []
            for i in range(size):
                front = q.popleft()
                level.append(front.val)
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
            traversal.append(level)
        return traversal[::-1]
