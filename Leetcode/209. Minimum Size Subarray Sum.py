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
        
        best = float('inf')
        
        i = 0
        window_sum = 0
        
        for j in range(len(nums)):
            window_sum += nums[j]
            while window_sum >= s:
                best = min(best, j-i+1)
                window_sum -= nums[i]
                i += 1
            
        return best if best != float('inf') else 0
