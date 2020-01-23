"""
199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        # return self.level_order(root)
        return self.dfs(root)
    
    def level_order(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        view = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            view.append(queue[-1].val)
            for i in range(size):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
        return view
    
    def dfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        view = []
        self.helper(root, view, 0)
        return view
    
    def helper(self, node, view, depth):
        if not node:
            return
        if depth == len(view):
            view.append(node.val)
        self.helper(node.right, view, depth+1)
        self.helper(node.left, view, depth+1)
