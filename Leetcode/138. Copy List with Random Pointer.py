"""
138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        curr = head
        
        while curr:
            real_next = curr.next
            curr.next = Node(curr.val, real_next, None)
            curr = curr.next.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
            
        old_list_ptr = head
        new_list_head = new_list_ptr = head.next
        
        while old_list_ptr:
            old_list_ptr.next = old_list_ptr.next.next
            new_list_ptr.next = new_list_ptr.next.next if new_list_ptr.next else None
            old_list_ptr = old_list_ptr.next
            new_list_ptr = new_list_ptr.next
        
        return new_list_head
