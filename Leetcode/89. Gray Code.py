"""
89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

Example 2:
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def backtrack(n):
            if n == 0:
                return ["0"]
            elif n == 1:
                return ["0", "1"]
            prev = backtrack(n-1)
            return ["0" + s for s in prev] + ["1" + s for s in reversed(prev)]
        return [int(d, 2) for d in backtrack(n)]
