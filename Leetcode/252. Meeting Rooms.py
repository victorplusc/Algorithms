"""
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""

# Time complexity: O(N log N)
# Space complexity: O(N)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i, interval in enumerate(intervals[:len(intervals)-1]):
            if interval[1] > intervals[i+1][0]:
                return False
        return True
