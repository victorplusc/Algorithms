"""
Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        q = collections.deque([root])
        levels = []
        rev = 0
        while q:
            level = []
            size = len(q)
            for i in range(size):
                front = q.popleft()
                level.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            if rev:
                level.reverse()
            rev = 1 - rev
            levels.append(level)
        return levels
