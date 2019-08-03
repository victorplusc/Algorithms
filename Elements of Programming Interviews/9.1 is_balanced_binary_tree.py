"""
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete binary tree. A height-balanced tree does not have to be perfect or complete.

Write a proogram that takes as input the root ofo a binary tree and checks whether the trtee is height-balanced.
"""

import collections

def is_balanced_binary_tree(root: TreeNode) -> bool:
    BalancedStatusWHeight = collections.namedtuple("BalancedStatusWHeight", ("balanced", "height"))
    
    def check_balanced(root):
        if not root:
            return BalancedStatusWHeight(True, -1)
        
        left_res = check_balanced(root.left)
        if not left_res.balanced:
            return BalancedStatusWHeight(False, 0)
        
        right_res = check_balanced(root.right)
        if not right_res.balanced:
            return BalancedStatusWHeight(False, 0)
        
        is_balanced = abs(left_res.height - right_res.height) <= 1
        height = max(left_res.height, right_res.height) + 1
        return BalancedStatusWHeight(is_balanced, height)

    return check_balanced(root).balanced
