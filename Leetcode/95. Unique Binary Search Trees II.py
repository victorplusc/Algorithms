"""
95. Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Constraints:
0 <= n <= 8
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(4**N/N**(1/2))
# Space complexity: O(4**N/N**(1/2))
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None,]
            all_trees = []
            for i in range(start, end+1):
                left_trees = generate(start, i-1)
                right_trees = generate(i+1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        curr = TreeNode(i)
                        curr.left = left
                        curr.right = right
                        all_trees.append(curr)
            return all_trees

        return generate(1, n) if n else []
