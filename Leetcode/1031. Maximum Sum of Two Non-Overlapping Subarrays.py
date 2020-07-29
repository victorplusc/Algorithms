"""
1031. Maximum Sum of Two Non-Overlapping Subarrays
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.

Example 1:
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 
Note:
L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # return self.prefix_sum(A, L, M)
        return self.sliding_window(A, L, M)
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def sliding_window(self, A, L, M):
        def max_sum(L, M):
            sum_L = sum_M = 0
            for i in range(0, L+M):
                if i < L:
                    sum_L += A[i]
                else:
                    sum_M += A[i]
            
            max_L, res = sum_L, sum_L+sum_M
            for i in range(L+M, len(A)):
                sum_L += A[i-M] - A[i-L-M]
                max_L = max(sum_L, max_L)
                sum_M += A[i] - A[i-M]
                res = max(res, max_L+sum_M)
            return res
        return max(max_sum(L, M), max_sum(M, L))
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def prefix_sum(self, A, L, M):
        def max_sum(L, M):
            max_L = res = 0
            for i in range(L+M, len(prefix_sum)):
                max_L = max(max_L, prefix_sum[i-M] - prefix_sum[i-L-M])
                res = max(res, max_L + prefix_sum[i] - prefix_sum[i-M])
            return res
        
        prefix_sum = [0] * (len(A)+1)
        for i, val in enumerate(A):
            prefix_sum[i+1] = prefix_sum[i] + val
        
        return max(max_sum(L, M), max_sum(M, L))
