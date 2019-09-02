"""
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""

class Solution:

# Time complexity: O(N)
# Space complexity: O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        curr = 0
        total = 0
        
        for num in nums:
            curr += num
            total += count.get(curr - k, 0)
            count[curr] = count.get(curr, 0) + 1
        
        return total

# Time complexity: O(N**2)
# Space complexity: O(1)
    def subarraySum_alt(self, nums: List[int], k: int) -> int:
        sum_count = 0
        for start in range(len(nums)):
            tmp_sum = 0
            for end in range(start, len(nums)):
                tmp_sum += nums[end]
                if tmp_sum == k:
                    sum_count += 1
        return sum_count
    
