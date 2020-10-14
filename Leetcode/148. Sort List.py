"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
# Time complexity: O(N log N)
# Space complexity: O(N log N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  
        
        prev, slow, fast = None, head, head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        
        def merge(A, B):
            dummy = ListNode(0)
            p = dummy
            
            while A and B:
                if A.val < B.val:
                    p.next = A
                    A = A.next
                else:
                    p.next = B
                    B = B.next
                p = p.next
            if A:
                p.next = A
            elif B:
                p.next = B
                
            return dummy.next
        
        return merge(left, right)
