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
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        
        while curr:
            real_next = curr.next
            curr.next = Node(curr.val, real_next, None)
            curr = curr.next.next
        
        curr = head
        while curr:
            return curr
