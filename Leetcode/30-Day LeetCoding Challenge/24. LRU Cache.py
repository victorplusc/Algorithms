"""
LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
class DoublyLinkedNode(object):
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.size = 0

        self.head = DoublyLinkedNode(None, None)
        self.tail = DoublyLinkedNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        node = self.cache.get(key, None)
        if node:
            self._move_node_to_front(node)
        return node.val if node else -1
    
    def _move_node_to_front(self, node):
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _pop_tail(self):
        tail = self.tail.prev
        self._remove_node(tail)
        return tail
    
    def put(self, key, val):
        node = self.cache.get(key)
        if not node:
            new_node = DoublyLinkedNode(key, val)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = val
            self._move_node_to_front(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
