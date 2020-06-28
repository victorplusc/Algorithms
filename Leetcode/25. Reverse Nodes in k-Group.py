"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.recursive(head, k)
        return self.iterative(head, k)
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def iterative(self, head, k):
        ptr = head
        ktail = None
        
        new_head = None
        
        while ptr:
            count = 0
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            
            if count == k:
                rev_head = self.reverse(head, k)
            
                if not new_head:
                    new_head = rev_head

                if ktail:
                    ktail.next = rev_head

                ktail = head
                head = ptr
        if ktail:
            ktail.next = head

        return new_head if new_head else head
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def recursive(self, head, k):
        count = 0
        ptr = head
        
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        if count == k:
            reversed_head = self.reverse(head, k)
            head.next = self.recursive(ptr, k)
            return reversed_head
        return head
    
    def reverse(self, head, k):
        new_head, ptr = None, head
        
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head
