"""
525. Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = {0: -1}
        longest = count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in mapping:
                longest = max(longest, i-mapping[count])
            else:
                mapping[count] = i
        return longest
