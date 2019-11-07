"""
303. Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
# Time complexity: O(1), for sumRange, O(N) pre-computation
# Space complexity: O(N)
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
