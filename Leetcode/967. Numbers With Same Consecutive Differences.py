"""
967. Numbers With Same Consecutive Differences
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:
1 <= N <= 9
0 <= K <= 9
"""
# Time complexity: O(N*2**N)
# Space complexity: O(2**N)
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        
        q = collections.deque([d for d in range(1, 10)])
        
        for level in range(N-1):
            size = len(q)
            for i in range(size):
                num = q.popleft()
                tail_digit = num%10
                next_digits = set([tail_digit+K, tail_digit-K])
                
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num*10 + next_digit
                        q.append(new_num)
        return q
