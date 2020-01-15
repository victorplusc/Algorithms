"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.generic_sliding_window(s)
        # return self.optimized(s)
        # return self.optimized_2(s)
        return self.optimized_3(s)
    
    def optimized(self, s):
        n = len(s)
        longest = 0
        seen = dict()
        i = 0
        for j in range(n):
            if s[j] in seen:
                i = max(seen[s[j]], i)
            longest = max(longest, j-i+1)
            seen[s[j]] = j+1
        return longest
    
    def optimized_2(self, s):
        n = len(s)
        longest = 0
        index = [0 for _ in range(128)]
        i = 0
        for j in range(n):
            i = max(index[ord(s[j])], i)
            longest = max(longest, j-i+1)
            index[ord(s[j])] = j + 1
        return longest

    def optimized_3(self, s):
        longest = left = 0
        seen = dict()
        for i, c in enumerate(s):
            if c in seen and left <= seen[c]:
                left = seen[c] + 1
            else:
                longest = max(longest, i-left+1)
            seen[c] = i
        return longest
        
    def generic_sliding_window(self, s):
        n = len(s)
        if n < 2: return n
        i = j = longest = 0
        seen = set()
        
        while j < n:
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1
                longest = max(longest, j-i)
        return longest
