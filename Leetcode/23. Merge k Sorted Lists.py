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

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        list_pointers = [node for node in lists]
        node_mapping = {}
        
        for i, node in enumerate(list_pointers):
            if node:
                node_mapping[i] = node
                heapq.heappush(min_heap, (node.val, i))
                
        head_node = ListNode(None)
        curr_node = head_node
        while min_heap:
            smallest_v, smallest_node_i = heapq.heappop(min_heap)
            smallest_node = node_mapping[smallest_node_i]
            curr_node.next = ListNode(smallest_v)
            curr_node = curr_node.next
            smallest_node = smallest_node.next
            if smallest_node != None:
                node_mapping[smallest_node_i] = smallest_node
                heapq.heappush(min_heap, (smallest_node.val, smallest_node_i))
        
        return head_node.next
