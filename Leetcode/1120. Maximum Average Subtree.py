"""
1120. Maximum Average Subtree
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:
Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.

Note:
The number of nodes in the tree is between 1 and 5000.
Each node will have a value between 0 and 100000.
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
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
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        def dfs(node):
            nonlocal best
            if not node:
                return 0, 0

            num_nodes = 1
            left, num_left = dfs(node.left)
            right, num_right = dfs(node.right)

            best = max( \
                best, \
                (node.val+left+right)/(num_nodes+num_left+num_right) \
            )

            return (node.val+left+right), (num_nodes+num_left+num_right)

        best = float('-inf')
        dfs(root)  
        return best
