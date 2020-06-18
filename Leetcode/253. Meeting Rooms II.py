"""
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        
        rooms = 0
        j = 0
        for i, start_time in enumerate(start):
            if end[j] <= start_time:
                rooms -= 1
                j += 1
            rooms += 1
        return rooms
    
#____________________________________________________________________ Old solutions

class Solution(object):
    def minMeetingRooms(self, intervals):
        #return self.heap_min_meeting_rooms(intervals)
        return self.ordering_min_meeting_rooms(intervals)
    
# Heap method
# Time complexiy: O(N log N)
# Space complexity: O(N)
    def heap_min_meeting_rooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key= lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])

        for i, interval in enumerate(intervals[1:]):
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, interval[1])
            
        return len(free_rooms)

# Chronological ordering method
# Time complexiy: O(N log N)
# Space complexity: O(N)
    def ordering_min_meeting_rooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])
        
        used_rooms = 0
        start_pointer = end_pointer = 0
        
        while start_pointer < len(intervals):
            if start_times[start_pointer] >= end_times[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1
            start_pointer += 1
            
        return used_rooms
