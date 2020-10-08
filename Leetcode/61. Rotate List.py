"""
61. Rotate List
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL

Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        curr = head
        ahead = head
        for i in range(k%n):
            ahead = ahead.next
        
        while ahead.next:
            curr = curr.next
            ahead = ahead.next
        
        ahead.next = head
        new_head = curr.next
        curr.next = None
        return new_head
