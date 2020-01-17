"""
159. Longest Substring with At Most Two Distinct Characters
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # return self.unoptimized(s)
        return self.optimized(s)

    def unoptimized(self, s):
        n = len(s)
        if n < 3:
            return n
        hashmap = collections.defaultdict()
        i = j = 0
        longest = 2
        
        while j < n:
            if s[j] in hashmap or len(hashmap) < 2:
                hashmap[s[j]] = hashmap[s[j]] + 1 if s[j] in hashmap else 1
                j += 1
            else:
                hashmap[s[i]] -= 1
                if hashmap[s[i]] == 0:
                    del hashmap[s[i]]
                i += 1
            longest = max(longest, j-i)
        
        return longest
    
    def optimized(self, s):
        left = longest = 0
        d = {}
        max_distinct = 2
        for right, char in enumerate(s):
            d[char] = right
            if len(d.keys()) == max_distinct + 1:
                rm_idx = min(d[char] for char in d.keys())
                d.pop(s[rm_idx], None)
                left = rm_idx + 1
            longest = max(longest, right-left + 1)
        return longest
