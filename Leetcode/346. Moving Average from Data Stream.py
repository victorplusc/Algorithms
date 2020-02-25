"""
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
# Time complexity: O(1)
# Space complexity: O(N)
class MovingAverage:

    # Deque
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = 0
        self.n = 0
        self.size = size
        self.nums = collections.deque()

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.n += 1
        self.sum += val
        if self.n > self.size:
            self.n -= 1
            self.sum -= self.nums.popleft()
        return self.sum/self.n

    # Circular array
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = 0
        self.n = 0
        self.size = size
        self.nums = [0] * size
        self.head = 0

    def next(self, val: int) -> float:
        self.n += 1
        tail = (self.head + 1) % self.size
        self.sum = self.sum - self.nums[tail] + val
        self.head = (self.head + 1) % self.size
        self.nums[self.head] = val
        return self.sum/min(self.size, self.n)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
