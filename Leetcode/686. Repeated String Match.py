"""
686. Repeated String Match
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
# Time complexity: O(A*B)
# Space complexity: O(A+B)
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        n = math.ceil(len(B)/len(A))
        new_word = A*n
        if B not in new_word:
            if B in new_word+A:
                return n+1
            else:
                return -1
        else:
            return n
