"""
337. House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # return self.naive(root)
        # return self.memoized(root, {})
        return max(self.dp(root))
    
    # Time complexity: O(~2**N)
    # Space complexity: O(N)
    def naive(self, node):
        if not node:
            return 0
        val = node.val
        
        if node.left:
            val += self.naive(node.left.right) + self.naive(node.left.left)
        if node.right:
            val += self.naive(node.right.left) + self.naive(node.right.right)

        return max(val, self.naive(node.left) + self.naive(node.right))
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def memoized(self, node, memo):
        if not node:
            return 0
        if node in memo:
            return memo[node]
        val = node.val
        if node.left:
            val += self.memoized(node.left.right, memo) + self.memoized(node.left.left, memo)
        if node.right:
            val += self.memoized(node.right.left, memo) + self.memoized(node.right.right, memo)

        memo[node] = max(val, self.memoized(node.left, memo) + self.memoized(node.right, memo))

        return memo[node]
    
    # Time complexity: O(N)
    # Space complexity: O(N), but O(1) excluding stack cost
    def dp(self, root):
        if not root:
            return [0, 0]
        
        left_inc, left_ex = self.dp(root.left)
        right_inc, right_ex = self.dp(root.right)
        curr_inc = root.val + left_ex + right_ex
        curr_ex = max(left_inc, left_ex) + max(right_inc, right_ex)
        
        return curr_inc, curr_ex
