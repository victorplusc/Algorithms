"""
738. Monotone Increasing Digits
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        S = [_ for _ in str(N)]
        monotone = True
        for i in range(len(S)-1):
            if S[i] > S[i+1]: 
                monotone = False
                break
        if monotone: return N
        
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1])-1)
            i -= 1
        S[i+1:] = "9" * (len(S) - i-1)
        
        return int("".join(S))
