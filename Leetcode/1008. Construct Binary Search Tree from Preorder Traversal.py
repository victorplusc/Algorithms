"""
1008. Construct Binary Search Tree from Preorder Traversal
Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.recursive(preorder)
        return self.iterative(preorder)
        
    # Time complexity: O(N)
    # Space complexity: O(N)
    def recursive(self, preorder):
        def helper(bound = float('inf')):
            nonlocal idx
            if idx == n:
                return None
            
            val = preorder[idx]
            if val > bound:
                return None
            
            idx += 1
            root = TreeNode(val)
            root.left = helper(val)
            root.right = helper(bound)
            return root
        
        idx = 0
        n = len(preorder)
        return helper()
    

    # Time complexity: O(N)
    # Space complexity: O(N)
    def iterative(self, preorder):
        if not preorder:
            return None
        n = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                node = stack.pop()
            
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root
