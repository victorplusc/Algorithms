"""
272. Closest Binary Search Tree Value II
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time complexity: O(N)
# Space complexity: O(K)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        q = collections.deque()
    
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            if len(q) < k:
                q.append(node.val)
            else:
                if abs(node.val - target) < abs(q[0] - target):
                    q.append(node.val)
                    q.popleft()
                else:
                    return

            inorder_traversal(node.right)

        inorder_traversal(root)
        return list(q)
