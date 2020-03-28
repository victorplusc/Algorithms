"""
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return self.recursive(root, p, q)
        # return self.iterative_parent_pointers(root, p, q)
        return self.iterative_no_parent_pointers(root, p, q)
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def recursive(self, root, p, q):
        self.ans = 0
    
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            mid = node == p or node == q
            
            if mid+left+right >= 2:
                self.ans = node
            return mid or left or right
        
        helper(root)
        return self.ans
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def iterative_parent_pointers(self, root, p, q):
        stack = [root]
        parent = {root: None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def iterative_no_parent_pointers(self, root, p, q):
        BOTH_PENDING = 2
        BOTH_VISITED = 0
        
        stack = [(root, BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1
        
        while stack:
            parent_node, parent_state = stack[-1]
            
            if parent_state != BOTH_VISITED:
                if parent_state == BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack)-1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state-1))
                if child_node:
                    stack.append((child_node, BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack)-1:
                    LCA_index -= 1
                stack.pop()
        return None
        
