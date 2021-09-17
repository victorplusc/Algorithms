"""
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
        if not root:
            return []

        queue = collections.deque([root])
        levels = []
        while queue:
            size = len(queue)
            current_level = []
            for _ in range(size):
                # we check if it's even because when it is, we are appending the next odd level
                if len(levels)%2 == 0: 
                    front = queue.popleft()
                    if front.left:
                        queue.append(front.left)
                    if front.right:
                        queue.append(front.right)
                else:
                    front = queue.pop()
                    if front.right:
                        queue.appendleft(front.right)
                    if front.left:
                        queue.appendleft(front.left)
                current_level.append(front.val)
            levels.append(current_level)
        return levels
