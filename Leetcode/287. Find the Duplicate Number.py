"""
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # return self.via_sort(nums)
        # return self.via_set(nums)
        return self.via_floyd(nums)
    
    # Time complexity: O(N log N)
    # Space complexity: O(1)
    def via_sort(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

    # Time complexity: O(N)
    # Space complexity: O(N)
    def via_set(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)

    # Time complexity: O(N)
    # Space complexity: O(1)
    def via_floyd(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        start = nums[0]
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        
        return start
