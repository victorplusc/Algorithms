"""
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palin(s):
            for i in range(len(s)//2):
                if s[i] != s[~i]:
                    return False
            return True
        
        def backtrack(start, end, curr):
            if start == end:
                partitions.append(curr[:])
            for i in range(start, end):
                new = s[start:i+1]
                if is_palin(new):
                    curr.append(new)
                    backtrack(i+1, end, curr)
                    curr.pop()
        
        partitions = []
        backtrack(0, len(s), [])
        return partitions
