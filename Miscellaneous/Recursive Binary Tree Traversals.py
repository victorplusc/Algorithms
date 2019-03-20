# Binary Tree Traversals (in-order, pre-order, post-order)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# In-order traversal
"""
In-order traversal means to 'visit' the left branch, then the current node, and finally the right branch.
When performed on a binary search tree, it visits the nodes in ascending order (hence the name 'in-order').
"""
def inOrderTraversal(node: "TreeNode"):
    if node != None:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)

# Pre-order traversal
"""
Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").
In a pre-order traversal, the root is always the first node visited.
"""
def preOrderTraversal(node: "TreeNode"):
    if node != None:
        visit(node)
        inOrderTraversal(node.left)
        inOrderTraversal(node.right)

# Post-order traversal
"""
Post-order traversal visits the current node after its child nodes (hence the name "post-order").
In a post-order traversal, the root is always the last node visited.
"""
def postOrderTraversal(node: "TreeNode"):
    if node != None:
        inOrderTraversal(node.left)
        inOrderTraversal(node.right)
        visit(node)

"""
#A placeholder function for any 'action' applied during the traversals
"""
def visit(node):
    pass
