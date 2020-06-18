"""
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if not intervals:
            return [new_interval]
        
        new_start, new_end = new_interval
        idx, n = 0, len(intervals)
        merged = []
        
        while idx < n and intervals[idx][0] < new_start:
            merged.append(intervals[idx])
            idx += 1
        
        if not merged or merged[-1][1] < new_start:
            merged.append(new_interval)
        else:
            merged[-1][1] = max(merged[-1][1], new_end)
        
        while idx < n:
            start, end = intervals[idx]
            if start > merged[-1][1]:
                merged.append(intervals[idx])
            else:
                merged[-1][1] = max(end, merged[-1][1])
            idx += 1
        return merged

# ----- If the intervals weren't merged to begin with:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if not intervals:
            return [new_interval]
        
        new_start, new_end = new_interval
        inserted = False
        if new_start < intervals[0][0]:
            start = new_start
            end = new_end
            inserted = True
        else:        
            start = intervals[0][0]
            end = intervals[0][1]
        
        merged = []
        i = 0
        while i < len(intervals):
            interval_start, interval_end = intervals[i][0], intervals[i][1]

            if not inserted and new_start < interval_start:
                interval_start, interval_end = new_interval
                inserted = True
                i -= 1
            
            if interval_start > end:
                merged.append([start, end])
                start = interval_start
                end = interval_end
            else:
                end = max(end, interval_end)
            i += 1
        
        if inserted:
            merged.append([start, end])
        else:
            if new_start > end:
                merged.append([start, end])
                merged.append(new_interval)
            else:
                end = max(end, new_end)
                merged.append([start, end])
            
        return merged
