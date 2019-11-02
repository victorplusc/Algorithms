"""
209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        min_len = float('inf')
        rolling_sum = 0
        i = 0
        
        for j in range(len(nums)):
            rolling_sum += nums[j]
            
            while rolling_sum - nums[i] >= s:
                rolling_sum -= nums[i]
                i += 1
                
            if rolling_sum >= s:
                min_len = min(min_len, j-i+1)
        
        return min_len if not min_len == float('inf') else 0
