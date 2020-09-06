"""
1574. Shortest Subarray to be Removed to Make Array Sorted
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

Example 4:
Input: arr = [1]
Output: 0

Constraints:
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l < r and arr[l+1] >= arr[l]:
            l += 1
        
        if l == len(arr) - 1:
            return 0
        
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        
        to_remove = min(len(arr)-l-1, r)
        
        for i in range(l+1):
            if arr[i] <= arr[r]:
                to_remove = min(to_remove, r-i-1)
            elif r < len(arr)-1:
                r += 1
            else:
                break
        return to_remove
