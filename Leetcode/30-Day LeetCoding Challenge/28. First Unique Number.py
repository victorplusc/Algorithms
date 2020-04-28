"""
First Unique Number
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:
Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:
Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:
Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
"""
class DoublyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FirstUnique:
    
    # Time complexity: O(N)
    def __init__(self, nums: List[int]):
        self.nodes = collections.defaultdict()
        self.count = collections.Counter(nums)
        
        self.head = DoublyLinkedNode(0)
        self.tail = DoublyLinkedNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
        for n in nums:
            if self.count[n] == 1:
                node = DoublyLinkedNode(n)
                self.nodes[n] = node
                self.add_to_tail(node)
    
    # Time complexity: O(1)
    def showFirstUnique(self) -> int:
        return self.head.next.val if self.head.next != self.tail else -1

    # Time complexity: O(1)
    def add(self, n: int) -> None:
        if n in self.count:
            if self.count[n] == 1:
                self.count[n] += 1
                self.remove_node(self.nodes[n])
        else:
            self.count[n] = 1
            node = DoublyLinkedNode(n)
            self.nodes[n] = node
            self.add_to_tail(node)
    
    # Time complexity: O(1)        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Time complexity: O(1)
    def add_to_tail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
