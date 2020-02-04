"""
152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # return self.linear_space(nums)
        return self.constant_space(nums)
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def linear_space(self, nums):
        rev = nums[::-1]
        for i in range(1, len(nums)):
            rev[i] *= rev[i-1] or 1
            nums[i] *= nums[i-1] or 1
            max_prod = max(rev[i], nums[i])
        return max(nums+rev)


    # Time complexity: O(N)
    # Space complexity: O(1)
    def constant_space(self, nums):
        max_prod = nums[0]
        idx_max = idx_min = max_prod
        for i in range(1, len(nums)):
            temp = (nums[i], idx_max*nums[i], idx_min*nums[i])
            idx_max = max(temp)
            idx_min = min(temp)
            max_prod = max(max_prod, idx_max)
        return max_prod
