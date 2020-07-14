"""
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        
        count1, candidate1 = 0, 0
        count2, candidate2 = 0, 0
        
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1-1, count2-1
                
        if candidate1 == candidate2:
            return [candidate1]
        else:
            return [candidate for candidate in (candidate1, candidate2) if nums.count(candidate) > len(nums)//3]
