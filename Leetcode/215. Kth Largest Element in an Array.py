# Time complexity: O(Nlog N)
# Space complexity: O(N)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        
        return heap[0]
