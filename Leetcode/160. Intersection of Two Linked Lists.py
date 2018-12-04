#160. Intersection of Two Linked Lists
"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA = headA
        currB = headB
        
        nodes = set()
        
        while currA != None:
            nodes.add(currA)
            currA = currA.next
            
        while currB != None:
            if currB in nodes:
                return currB
            nodes.add(currB)
            currB = currB.next
        
        return None
