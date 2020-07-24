"""
727. Minimum Window Subsequence
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:
Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

Note:
All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""
# Time complexity: O(N*M), amortized O(N)
# Space complexity: O(M)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n, m = len(S), len(T)
        
        mapping = collections.defaultdict(list)
        for i, c in enumerate(T):
            mapping[c].append(i)
        
        dp = [-1 for i in range(m)]
        
        best = n+1
        start = -1
        for index, c in enumerate(S):
            if c in mapping:
                for i in mapping[c][::-1]:
                    if i == 0:
                        dp[i] = index
                    else:
                        dp[i] = dp[i-1]
                    if i == m-1 and dp[i] >= 0 and index - dp[i]+1 < best:
                        best = index - dp[i] + 1
                        start = dp[i]
        return "" if dp[-1] < 0 else S[start:start+best]
