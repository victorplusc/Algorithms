"""
Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: 
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
"""
# Time complexity: O(N+M)
# Space complexity: O(N+M)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ptr_a = ptr_b = 0
        intervals = []
        while ptr_a < len(A) and ptr_b < len(B):
            start = max(A[ptr_a][0], B[ptr_b][0])
            end = min(A[ptr_a][1], B[ptr_b][1])
            
            if start <= end:
                intervals.append([start, end])
            
            if A[ptr_a][1] < B[ptr_b][1]:
                ptr_a += 1
            else:
                ptr_b += 1
        
        return intervals
