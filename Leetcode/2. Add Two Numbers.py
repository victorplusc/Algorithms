"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time complexity: O(max(N+M))
# Space complexity: O(max(N+M))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p, q, curr = l1, l2, head
        carry = 0
        
        while p or q:
            if p == None: 
                x = 0
            else: 
                x = p.val
                
            if q == None: 
                y = 0
            else: 
                y = q.val
            
            node_val = x + y + carry
            carry = node_val//10
            
            curr.next = ListNode(node_val % 10)
            curr = curr.next
            
            if p: p = p.next
            if q: q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return head.next
