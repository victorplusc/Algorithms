"""
1286. Iterator for Combination
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.

Example:
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:
1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.q = collections.deque()
        self._generate_combinations(characters, 0, "", combinationLength)

    def next(self) -> str:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q) > 0
        
    def _generate_combinations(self, characters, start, curr, k):
        if k == 0:
            self.q.append(curr)
            return
        for i in range(start, len(characters)):
            self._generate_combinations(characters, i+1, curr+characters[i], k-1)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
