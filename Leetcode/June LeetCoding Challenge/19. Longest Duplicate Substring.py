"""
Longest Duplicate Substring
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

Example 1:
Input: "banana"
Output: "ana"

Example 2:
Input: "abcd"
Output: ""

Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
"""
# Time complexity: O(N log N)
# Space complexity: O(N)
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        
        nums = [ord(c)-ord('a') for c in s]
        base = 26
        mod = 2**32
        
        left, right = 1, n
        while left < right:
            mid = (left+right)//2
            if self.rabin_karp(mid, base, mod, n, nums) != -1:
                left = mid + 1
            else:
                right = mid
        
        start = self.rabin_karp(left-1, base, mod, n, nums)
        end = start+left-1
        return s[start:end]
    
    def rabin_karp(self, mid, base, mod, n, nums):
        h = 0
        for i in range(mid):
            h = (h*base+nums[i]) % mod
        
        seen = {h}
        base_len = pow(base, mid, mod)
        for start in range(1, n-mid+1):
            h = (h * base-nums[start - 1] * base_len + nums[start + mid - 1]) % mod
            if h in seen:
                return start
            seen.add(h)
        return -1
