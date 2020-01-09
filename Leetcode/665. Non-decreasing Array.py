"""
665. Non-decreasing Array
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def checkPossibility(self, A: List[int]) -> bool:
        p = None
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i
        return p is None or p == 0 or p == len(A)-2 or A[p-1] <= A[p+1] or A[p] <= A[p+2]
