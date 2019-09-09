# Time complexity: O(Nlog N)
# Space complexity: O(N)
# Unoptimized
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = []
        
        for i in nums:
            heapq.heappush(max_heap, -i)
        
        for i in range(k-1):
            heapq.heappop(max_heap)
        
        return -heapq.heappop(max_heap)
