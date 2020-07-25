"""
1525. Number of Good Ways to Split a String
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def numSplits(self, s: str) -> int:
        def is_splittable(left, total):
            return len(left) == len([c for c in total if total[c] > 0])
        total = collections.Counter(s)
        good_splits = 0
        left = set()
        for i in range(len(s)):
            if is_splittable(left, total):
                good_splits += 1
            left.add(s[i])
            total[s[i]] -= 1
        return good_splits
