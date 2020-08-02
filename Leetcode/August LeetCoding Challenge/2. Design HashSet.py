"""
Design HashSet
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 769
        self.bucket_list = [Bucket() for _ in range(self.mod)]
        

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        self.bucket_list[bucket_idx].insert(key)
        
    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        self.bucket_list[bucket_idx].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket_idx = self._hash(key)
        return self.bucket_list[bucket_idx].exists(key) 

    def _hash(self, key):
        return key%self.mod

class Node():
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
    
class Bucket():
    def __init__(self):
        self.head = Node(0)
        
    def insert(self, new_val):
        if not self.exists(new_val):
            new_node = Node(new_val, self.head.next)
            self.head.next = new_node
    
    def delete(self, val):
        prev = self.head
        curr = self.head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
