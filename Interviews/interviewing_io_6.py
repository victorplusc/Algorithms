"""
Design a data structure that supports the following three operations. 

1. a constructor that takes a parameter K 
2. add(x) -- inserts the number x 
3. get() -- returns the product of the last K elements inserted 
"""
class LastKProduct():
    def __init__(self, K):
        self.K = K
        self.curr_prod = 1
        self.nums = collections.deque()
        self.zeroes = 0
    
    def __multiply_all(self):
        self.curr_prod = 1
        for val in self.nums:
            self.curr_prod *= val
    
    def add(self, x):
        if x == 0:
            self.zeroes += 1
        self.curr_prod *= x
        self.nums.append(x)
        if len(self.nums) > self.K:
            to_divide = self.nums.popleft()
            if to_divide:
                self.curr_prod /= to_divide
            else:
                self.zeroes -= 1
                if self.zeroes == 0:
                    self.__multiply_all()
    
    def get(self):
        return self.curr_prod

# Design a data structure that supports the following two operations. 
# 1. add(x) -- inserts the number x 
#
# 2. get(K) -- returns the product of the last K elements inserted 

class LastKProducts():
    def __init__(self):
        self.cumulative = []
        self.last_zero = -1
    
    def add(self, x):
        if x == 0:
            self.last_zero = len(self.cumulative)
        if self.cumulative:
            front = self.cumulative[-1]
            if front == 0:
                self.cumulative.append(x)
            else:
                self.cumulative.append(x*front)
        else:
            self.cumulative.append(x)
    
    def get(self, k):
        front = self.cumulative[-1]
        if not front: 
            return 0
        if self.last_zero >= len(self.cumulative)-k:
            return 0
        if not self.cumulative[-1-k]: 
            return front
        return front//self.cumulative[-1-k]
