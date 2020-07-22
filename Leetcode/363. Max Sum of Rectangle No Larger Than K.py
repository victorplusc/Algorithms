"""
363. Max Sum of Rectangle No Larger Than K
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""
# Time complexity: O(N**2*M**2)
# Space complexity: O(N)
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        
        n, m = len(matrix), len(matrix[0])
        res = float('-inf')
        for i in range(m):
            sums = [0]*n
            for j in range(i, m):
                for y in range(n):
                    sums[y] += matrix[y][j]
                
                cumulative_sums = [0]
                curr_sum = 0
                curr_max = float('-inf')
                for val in sums:
                    curr_sum += val
                    left = bisect.bisect_left(cumulative_sums, curr_sum-k)
                    if left < len(cumulative_sums):
                        curr_max = max(curr_max, curr_sum - cumulative_sums[left])
                    bisect.insort(cumulative_sums, curr_sum)
                res = max(res, curr_max)
        return res
    
