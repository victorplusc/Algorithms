"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        is_palindrome = True
        first = head
        second = prev
        while is_palindrome and second:
            if first.val != second.val:
                is_palindrome = False
            first = first.next
            second = second.next
        
        return is_palindrome
