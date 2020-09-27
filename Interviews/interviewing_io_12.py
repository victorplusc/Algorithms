# You are given a binary tree, to output the number of paths that have a given sum.

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_paths(root, k):
    total = 0
    def helper(node, prev):
        if not node:
            return
        nonlocal total

        prev.append(0)
        for i in range(len(prev)):
            prev[i] += node.val
            total += prev[i] == k
        
        helper(node.left, prev[:])
        helper(node.right, prev[:])
    
    helper(root, [])
    return total
    
root = TreeNode(8)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(-8)

root.right = TreeNode(5)
root.right.left = TreeNode(2)
root.right.left.right = TreeNode(5)
root.right.left.right.right = TreeNode(0)

root.right.right = TreeNode(6)

print(binary_tree_paths(root, 7))
