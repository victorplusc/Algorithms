"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.greedy(nums)
        return self.dp(nums)
        return self.recursive(nums)
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def greedy(self, nums):
        curr_sum = max_sum = nums[0]
        for n in nums[1:]:
            curr_sum = max(n, curr_sum+n)
            max_sum = max(curr_sum, max_sum)
        return max_sum

    # Time complexity: O(N)
    # Space complexity: O(1)
    def dp(self, nums):
        n = len(nums)
        max_sum = nums[0]
        
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)
        return max_sum

    # Time complexity: O(N log N)
    # Space complexity: O(1)
    def recursive(self, nums):
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        prt = (left+right)//2
        left_sum = self.helper(nums, left, prt)
        right_sum = self.helper(nums, prt+1, right)
        cross_sum = self.cross_sum(nums, left, right, prt)
        return max(left_sum, right_sum, cross_sum)
    
    def cross_sum(self, nums, left, right, prt):
        if left == right:
            return nums[left]
        
        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(prt, left-1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)
        
        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(prt+1, right+1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)
        return left_subsum + right_subsum
