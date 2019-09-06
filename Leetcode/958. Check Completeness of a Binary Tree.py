"""
958. Check Completeness of a Binary Tree
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time complexity: O(N)
# Space complexity: O(N)
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                break
            elif node.left == None:
                if node.right != None:
                    return False
                break
            queue.append(node.left)
            if node.right == None: break
            queue.append(node.right)
        
        while queue:
            node = queue.pop(0)
            if node.left != None or node.right != None:
                return False
            
        return True
