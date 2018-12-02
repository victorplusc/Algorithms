#206. Reverse Linked List
"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while (curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
