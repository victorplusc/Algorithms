"""
Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:

    # Time complexity: O(N)
    # Space complexity: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right_prod = [0 for _ in range(n)]
        left_prod = [0 for _ in range(n)]
        output = [0 for _ in range(n)]
        
        left_prod[0] = 1
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]
        
        right_prod[-1] = 1
        for i in reversed(range(n-1)):
            print(i)
            right_prod[i] = right_prod[i+1] * nums[i+1]
        
        for i in range(n):
            output[i] = left_prod[i] * right_prod[i]
            
        return output

    # Time complexity: O(N)
    # Space complexity: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0 for _ in range(n)]
        
        output[0] = 1
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        
        right_prod = 1
        for i in reversed(range(n)):
            output[i] *= right_prod
            right_prod *= nums[i]
            
        return output
