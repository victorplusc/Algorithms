"""
109. Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.simulation(head)
        return self.cast_to_list(head)
        return self.finding_middle_of_list(head)
    
    # Time complexity: O(N)
    # Space complexity: O(log N)
    def simulation(self, head):
        size = self.find_size(head)
        
        def convert(left, right):
            nonlocal head
            
            if left > right:
                return None
            mid = (left+right)//2
            
            left = convert(left, mid-1)
            
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            
            node.right = convert(mid+1, right)
            return node
        
        return convert(0, size-1)
    
    def find_size(self, head):
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        return size
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def cast_to_list(self, head):
        order = self.to_list(head)
        def convert_to_bst(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            node = TreeNode(order[mid])
            
            if left == right:
                return node
            
            node.left = convert_to_bst(left, mid-1)
            node.right = convert_to_bst(mid+1, right)
            return node
        return convert_to_bst(0, len(order)-1)
    
    def to_list(self, head):
        curr = head
        new = []
        while curr:
            new.append(curr.val)
            curr = curr.next
        return new
    
    # Time complexity: O(N log N)
    # Space complexity: O(log N)
    def finding_middle_of_list(self, head):
        if not head:
            return None
        
        mid = self.find_mid(head)
        node = TreeNode(mid.val)
        
        if head == mid:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
    
    def find_mid(self, head):
        prev = None
        slow = fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        
        return slow
