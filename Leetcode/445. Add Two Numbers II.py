"""
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        stack1 = []
        stack2 = []
        
        while curr1:
            stack1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next
            
        carry = 0
        sum_node = ListNode(0)
        while stack1 or stack2:
            n1 = stack1.pop() if stack1 else 0
            n2 = stack2.pop() if stack2 else 0
            sum_node.val = (n1+n2+carry)%10
            carry = (n1+n2+carry)//10
            head = ListNode(carry)
            head.next = sum_node
            sum_node = head

        return sum_node.next if sum_node.val == 0 else sum_node
