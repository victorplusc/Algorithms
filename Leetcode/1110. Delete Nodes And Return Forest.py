"""
1110. Delete Nodes And Return Forest
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.forest = []
        self.to_delete = set(to_delete)
        self.dfs(root, True)
        return self.forest
    
    def dfs(self, root, is_root):
        if not root:
            return
        if root.val in self.to_delete:
            root.left = self.dfs(root.left, True)
            root.right = self.dfs(root.right, True)
            return
        
        if is_root:
            self.forest.append(root)
        root.left = self.dfs(root.left, False)
        root.right = self.dfs(root.right, False)
        
        return root
