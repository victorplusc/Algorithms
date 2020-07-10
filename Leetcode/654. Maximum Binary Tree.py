"""
654. Maximum Binary Tree
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Note:
The size of the given array will be in the range [1,1000].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # return self.naive(nums)
        return self.optimized(nums)
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def optimized(self, nums):
        stack = []
        for val in nums:
            node = TreeNode(val)
            while stack and val > stack[-1].val:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
    
    # Time complexity: O(N**2)
    # Space complexity: O(N)
    def naive(self, nums):
        if not nums: return None
        local_max, idx = self.find_maximum_index(nums)
        root = TreeNode(local_max)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root

    def find_maximum_index(self, nums):
        local_max, idx = -float('inf'), -1
        for i, v in enumerate(nums):
            if v > local_max:
                local_max = v
                idx = i
        return local_max, idx
