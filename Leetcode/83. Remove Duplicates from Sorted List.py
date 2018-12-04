#83. Remove Duplicates from Sorted List
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        
        while curr != None and curr.next != None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head
