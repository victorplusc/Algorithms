"""
340. Longest Substring with At Most K Distinct Characters
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if n == k:
            return n
        i = longest = 0
        indices = {}
        for j in range(n):
            indices[s[j]] = j
            if len(indices) == k+1:
                rm_idx = min(indices[idx] for idx in indices)
                indices.pop(s[rm_idx])
                i = rm_idx + 1
            longest = max(longest, j-i+1)
        return longest
