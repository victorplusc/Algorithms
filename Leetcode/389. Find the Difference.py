"""
389. Find the Difference
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = ord(t[-1])
        
        for c1, c2 in zip(s, t):
            s_sum += ord(c1)
            t_sum += ord(c2)
        
        return chr(t_sum-s_sum)
