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

# Time complexity: O(N)
# Space complexity: O(N)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ",".join(self.serialize_helper(root, []))
        
    def serialize_helper(self, root, serialized):
        if not root:
            serialized.append("X")
        else:
            serialized.append(str(root.val))
            self.serialize_helper(root.left, serialized)
            self.serialize_helper(root.right, serialized)
        return serialized
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = self.deserialize_helper(data.split(","))
        return root
    
    def deserialize_helper(self, data):
        if data[0] == "X":
            data.pop(0)
            return None
        root = TreeNode(int(data.pop(0)))
        root.left = self.deserialize_helper(data)
        root.right = self.deserialize_helper(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
