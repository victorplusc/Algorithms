class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#Iterative in-order traversal
def inorderTraversal(self, root):
    stack = []
    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if stack != []:
                root = stack.pop()
                visit(root)
                root = root.right
            else:
                break

"""
#A placeholder function for any 'action' applied during the traversals
"""
def visit(node):
    pass
