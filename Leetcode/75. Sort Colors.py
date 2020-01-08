"""
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.double_pass(nums)
        self.single_pass(nums)


    # Time complexity: O(N)
    # Space complexity: O(1)
    def single_pass(self, nums):
        left = curr = 0
        right = len(nums)-1
        
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1


    # Time complexity: O(N)
    # Space complexity: O(1)
    def double_pass(self, nums):
        zeroes = 0
        ones = 0
        twos = 0
        for n in nums:
            if n == 0:
                zeroes += 1
            if n == 1:
                ones += 1
            if n == 2:
                twos += 1
        for i in range(len(nums)):
            if zeroes > 0:
                nums[i] = 0
                zeroes -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            elif twos > 0:
                nums[i] = 2
                twos -= 1
