"""
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections
class Solution:
    
    # Time complexity: O(|S| + |T|)
    # Space complexity: O(|S| + |T|)
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        req_chars = collections.Counter(t)
        req_size = len(req_chars)
        window = collections.Counter()
        min_size = (float('inf'), -1, -1)
        curr_seen = 0
        i = 0
        for j in range(len(s)):
            window[s[j]] += 1
            if s[j] in req_chars and window[s[j]] == req_chars[s[j]]:
                curr_seen += 1
            
            while i <= j and curr_seen == req_size:
                if j - i + 1 < min_size[0]:
                    min_size = (j - i + 1, i, j)
                
                window[s[i]] -= 1
                if s[i] in req_chars and window[s[i]] < req_chars[s[i]]:
                    curr_seen -= 1
                
                i += 1
        
        return "" if min_size[0] == float('inf') else s[min_size[1] : min_size[2] + 1]
    
    
##### Optimized approach, better when |S| >> |filtered_s|
    # Time complexity: O(|S| + |T|)
    # Space complexity: O(|S| + |T|)
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        req_chars = collections.Counter(t)
        req_size = len(req_chars)
        filtered_s = []
        for i, c in enumerate(s):
            if c in req_chars:
                filtered_s.append((i, c))
        
        window = collections.Counter()
        i = 0
        curr_seen = 0
        min_size = (float('inf'), -1, -1)
        
        for j in range(len(filtered_s)):
            c = filtered_s[j][1]
            window[c] += 1
            if window[c] == req_chars[c]:
                curr_seen += 1
            while i <= j and curr_seen == req_size:
                c = filtered_s[i][1]
                end = filtered_s[j][0]
                start = filtered_s[i][0]
                if end-start+1 < min_size[0]:
                    min_size = (end-start+1, start, end)
                
                window[c] -= 1
                if window[c] < req_chars[c]:
                    curr_seen -= 1
                i += 1
                
        return "" if min_size[0] == float('inf') else s[min_size[1]:min_size[2]+1]
