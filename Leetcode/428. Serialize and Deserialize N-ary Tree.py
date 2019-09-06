"""
428. Serialize and Deserialize N-ary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Time complexity: O(N)
# Space complexity: O(N)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serialized = []
        self.serialize_helper(root, serialized)
        return " ".join(serialized)
    
    def serialize_helper(self, root, serialized):
        if root:
            serialized.append(str(root.val))
            for node in root.children:
                self.serialize_helper(node, serialized)
                serialized.append("/") 
        else:
            serialized.append("X")
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        deserialized = data.split(" ")
        return self.deserialize_helper(deserialized)
    
    
    def deserialize_helper(self, deserialized):
        if deserialized:
            if deserialized[0] == "X":
                deserialized.pop(0)
                return None
            
            root = Node(int(deserialized.pop(0)), []) 
            while deserialized and deserialized[0] != "/":
                node = self.deserialize_helper(deserialized)
                root.children.append(node)

            if deserialized and deserialized[0] == "/":
                deserialized.pop(0)

            return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
