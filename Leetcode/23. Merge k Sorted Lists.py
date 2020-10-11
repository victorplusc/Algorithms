# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
23. Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Time complexity: O(N log k), where N is the length of the final list and k is the number of lists
# Space complexiy: O(k)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            if node.next:
                # recycling i guarantees uniqueness against tie-breaker in heapq when two node values are the same
                heapq.heappush(heap, (node.next.val, i, node.next)) 
            curr.next = node
            curr = curr.next
        return dummy.next
