"""
Maximum Width of Binary Tree
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return self.bfs(root)
        return self.dfs(root)
    
    def dfs(self, root):
        first_col_idxes = {}
        max_width = 0
        
        def dfs(node, depth, col_idx):
            nonlocal max_width
            if not node: return
            
            if depth not in first_col_idxes:
                first_col_idxes[depth] = col_idx
            
            max_width = max(max_width, col_idx-first_col_idxes[depth]+1)
                
            dfs(node.left, depth+1, col_idx*2)
            dfs(node.right, depth+1, col_idx*2+1)

        dfs(root, 0, 0)
        return max_width
        
    def bfs(self, root):
        max_width = 0
        q = collections.deque([(root, 0)])
        while q:
            size = len(q)
            level_head_index = q[0][1]
            for _ in range(size):
                node, col_index = q.popleft()
                
                if node.left:
                    q.append((node.left, 2*col_index))
                if node.right:
                    q.append((node.right, 2*col_index+1))
            max_width = max(max_width, col_index-level_head_index+1)
        
        return max_width
