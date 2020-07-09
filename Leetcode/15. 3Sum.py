"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.two_pointers(nums)
        return self.hash_set(nums)
    
    # Time complexity: O(N**2)
    # Space complexity: O(N**2)
    def hash_set(self, nums):
        n = len(nums)
        seen = {}
        found, dupes = set(), set()
        
        sums = []
        for i in range(n):
            if nums[i] not in dupes: 
                dupes.add(nums[i])
                
                for j in range(i+1, n):
                    complement = -nums[i] - nums[j]
                    if complement in seen and seen[complement] == i:
                        min_val = min(nums[i], nums[j], complement)
                        max_val = max(nums[i], nums[j], complement)
                        if (min_val, max_val) not in found:
                            found.add((min_val, max_val))
                            sums.append([nums[i], nums[j], complement])
                    seen[nums[j]] = i
        return sums
    
    # Time complexity: O(N**2)
    # Space complexity: O(N)
    def two_pointers(self, nums):
        n = len(nums)
        nums.sort()
        
        sums = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.two_sum(nums, i, sums)
        return sums
    
    def two_sum(self, nums, i, sums):
        left, right = i+1, len(nums)-1
        
        while left < right:
            curr = nums[i] + nums[left] + nums[right]
            
            if curr < 0 or (left > i+1 and nums[left] == nums[left-1]):
                left += 1
            elif curr > 0 or (right < len(nums)-1 and nums[right] == nums[right+1]):
                right -= 1
            else:
                sums.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
