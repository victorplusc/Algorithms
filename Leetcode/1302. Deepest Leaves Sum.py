"""
1302. Deepest Leaves Sum
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = collections.deque([root])
        
        while q:
            size = len(q)
            curr = 0
            not_lowest = False
            for _ in range(size):
                front = q.popleft()
                curr += front.val
                if front.left or front.right:
                    not_lowest = True
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            if not not_lowest:
                return curr
