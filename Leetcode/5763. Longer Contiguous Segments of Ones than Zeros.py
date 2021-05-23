"""
5763. Longer Contiguous Segments of Ones than Zeros
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.
"""
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        curr_0s = curr_1s = best_0s = best_1s = 0

        for c in s:
            if c == "0":
                curr_0s += 1
                best_1s = max(best_1s, curr_1s)
                curr_1s = 0
            else:
                curr_1s += 1
                best_0s = max(best_0s, curr_0s)
                curr_0s = 0
                
        best_0s = max(best_0s, curr_0s)
        best_1s = max(best_1s, curr_1s)
        return best_1s > best_0s
