"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        queue = [root]
        while queue:
            front = queue.pop()
            if front:
                queue.insert(0, front.left)
                queue.insert(0, front.right)
                serialized.append(front.val)
            else:
                serialized.append(front)
        return serialized
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data.reverse()
        data_tree = curr = TreeNode(None)
        data_tree.left = TreeNode(None)
        data_tree.right = None
        
        while data:
            front = data.pop()
            new = TreeNode(front)
            if len(data) > 1 and data[-1]:
                new.left = TreeNode(data[-1])
            if len(data) > 2 and data[-2]:
                new.right = TreeNode(data[-1])
            if not data_tree.left:
                data_tree.left = new
                data_tree = data_tree.left
            else:
                data_tree.right = new
                data_tree = data_tree.right
        
        return curr.right
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
