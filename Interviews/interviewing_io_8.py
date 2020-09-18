def inorderTraversal(self, root):
    stack = []
    traversal = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        traversal.append(node.val)
        root = node.right
    return traversal
