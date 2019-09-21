"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class Node():
    def __init__(self, val, curr_min):
        self.val = val
        self.min = curr_min

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            new_node = Node(x, x)
            self.stack.append(new_node)
        else:
            new_min = min(x, self.stack[-1].min)
            self.stack.append(Node(x, new_min))
        

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop().val
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].val
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1].min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
