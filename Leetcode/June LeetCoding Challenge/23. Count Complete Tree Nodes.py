# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        d = self.find_depth(root)
        
        if d == 0: return 1
        
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = (left+right)//2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2**d-1) + left
    
    def exists(self, idx, d, node):
        left, right = 0, 2**d-1
        for _ in range(d):
            pivot = (left+right)//2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def find_depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d
