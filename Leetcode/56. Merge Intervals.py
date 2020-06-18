"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
# Time complexity: O(N log N)
# Space complexity: O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        merged = []
        
        for new_start, new_end in intervals[1:]:
            if new_start > end:
                merged.append([start, end])
                start = new_start
                end = new_end
            else:
                end = max(end, new_end)
        
        merged.append([start, end])
        return merged
