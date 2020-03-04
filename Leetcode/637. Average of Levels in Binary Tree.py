"""
637. Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        return self.dfs(root)
        return self.bfs(root)
    
    def dfs(self, root):
        count = []
        res = []
        self.helper(root, 0, res, count)
        res = [res[i]/count[i] for i in range(len(res))]
        return res
    
    def helper(self, node, depth, res, count):
        if not node:
            return
        if depth < len(res):
            res[depth] += node.val
            count[depth] += 1
        else:
            res.append(node.val)
            count.append(1)
        self.helper(node.left, depth+1, res, count)
        self.helper(node.right, depth+1, res, count)
    

    def bfs(self, root):
        if not root:
            return [0]
        levels = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            curr = 0
            for i in range(size):
                front = queue.popleft()
                curr += front.val
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            levels.append(curr/size)
        return levels
