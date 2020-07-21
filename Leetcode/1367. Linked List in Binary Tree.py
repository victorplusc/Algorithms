"""
1367. Linked List in Binary Tree
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

Constraints:
1 <= node.val <= 100 for each node in the linked list and binary tree.
The given linked list will contain between 1 and 100 nodes.
The given binary tree will contain between 1 and 2500 nodes.
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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # return self.recursive(head, root)
        return self.dp(head, root)
    
    # Time complexity: O(N)
    # Space complexity: O(L+H)
    def dp(self, head, root):
        A = [head.val]
        dp = [0]
        
        i = 0
        curr = head.next
        while curr:
            while i > 0 and curr.val != A[i]:
                i = dp[i-1]
            if curr.val == A[i]:
                i += 1
            A.append(curr.val)
            dp.append(i)
            curr = curr.next
        
        def dfs(root, i):
            if not root: return False
            while i and root.val != A[i]:
                i = dp[i-1]
            if root.val == A[i]:
                i += 1
            return i == len(dp) or dfs(root.left, i) or dfs(root.right, i)
        return dfs(root, 0)
    
    # Time complexity: O(N*min(L, H))
    # Space complexity: O(H)
    def recursive(self, head, root):
        def dfs(curr, root):
            if not curr: return True
            if not root: return False
            left = dfs(curr.next, root.left)
            right = dfs(curr.next, root.right)
            return curr.val == root.val and (left or right)
        if not head: return True
        if not root: return False 
        return dfs(head, root) or self.recursive(head, root.left) or self.recursive(head, root.right)
