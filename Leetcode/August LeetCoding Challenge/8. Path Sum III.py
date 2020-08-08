"""
Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
    def pathSum(self, root: TreeNode, target: int) -> int:
        seen = {0:1}
        self.res = 0
        self.dfs(root, target, 0, seen)
        return self.res
    
    def dfs(self, root, target, curr, seen):
        if not root:
            return
        curr += root.val
        old = curr-target
        self.res += seen.get(old, 0)
        seen[curr] = seen.get(curr, 0) + 1
        self.dfs(root.left, target, curr, seen)
        self.dfs(root.right, target, curr, seen)
        seen[curr] -= 1
    
