"""
173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(H)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.__inorder_left(root)

    def __inorder_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack.pop()
        if top.right:
            self.__inorder_left(top.right)
        return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Time complexity: O(N)
# Space complexity: O(N)
class BSTIterator_Naive:

    def __init__(self, root: TreeNode):
        self.sorted_nodes = []
        self.idx = -1
        self.__inorder(root)
        self.size = len(self.sorted_nodes)

    def __inorder(self, root):
        if not root: return
        self.__inorder(root.left)
        self.sorted_nodes.append(root.val)
        self.__inorder(root.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.idx += 1
        return self.sorted_nodes[self.idx] if self.idx < self.size else -1

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.idx + 1 < self.size

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
