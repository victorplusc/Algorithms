"""
1526. Minimum Number of Increments on Subarrays to Form a Target Array
Given an array of positive integers target and an array initial of same size with all zeros.

Return the minimum number of operations to form a target array from initial if you are allowed to do the following operation:

Choose any subarray from initial and increment each value by one.
The answer is guaranteed to fit within the range of a 32-bit signed integer.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total = target[0]
        
        for i in range(1, len(target)):
            if target[i-1] < target[i]:
                total += target[i] - target[i-1]
        return total
