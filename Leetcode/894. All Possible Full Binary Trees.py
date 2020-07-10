"""
894. All Possible Full Binary Trees
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

Note:
1 <= N <= 20
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        elif N == 1:
            return [TreeNode(0)]
        
        output = []
        for i in range(2, N+1, 2):
            left_trees = self.allPossibleFBT(i-1)
            right_trees = self.allPossibleFBT(N-i)
            for left_idx, left_branch in enumerate(left_trees, 1):
                for right_idx, right_branch in enumerate(right_trees, 1):
                    tree = TreeNode(0)
                    
                    tree.left = self.clone(left_branch) if right_idx < len(right_trees) else left_branch
                    tree.right = self.clone(right_branch) if left_idx < len(left_trees) else right_branch
                    output.append(tree)
        return output
    
    def clone(self, node):
        if not node: return None
        tree = TreeNode(node.val)
        tree.left = self.clone(node.left)
        tree.right = self.clone(node.right)
        return tree
