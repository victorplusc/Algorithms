"""
220. Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

Constraints:
0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        buckets = {}
        bucket_size = t+1
        
        for i in range(len(nums)):
            bucket_num = nums[i]//bucket_size
            
            if bucket_num in buckets:
                return True
            
            if bucket_num-1 in buckets and abs(nums[i] - buckets[bucket_num-1]) <= t:
                return True
            if bucket_num+1 in buckets and abs(nums[i] - buckets[bucket_num+1]) <= t:
                return True
            
            buckets[bucket_num] = nums[i]
            if i >= k:
                del buckets[nums[i-k]//bucket_size]
        return False
        
