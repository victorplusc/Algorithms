"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    #Write your code here
    def helper(root):
        if not root: return
        helper(root.left)
        order.append(str(root.info))
        helper(root.right)
    order = []
    helper(root)
    print(" ".join(order))
