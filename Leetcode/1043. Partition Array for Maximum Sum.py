"""
1043. Partition Array for Maximum Sum
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

Example 1:
Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]

Note:
1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
"""
# Time complexity: O(N*K)
# Space complexity: O(N)
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n+1)
        for i in range(n):
            curr_max = 0
            _range = range(1, min(K, i+1)+1)
            for k in _range:
                curr_max = max(curr_max, A[i-k+1])
                dp[i] = max(dp[i], dp[i-k]+curr_max*k)
        return dp[n-1]
