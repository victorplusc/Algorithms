"""
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
             
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
# Time complexity: O(N**2)
# Space complexity: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.backtrack(s, wordDict)
        # return self.bfs(s, wordDict)
        return self.dp(s, wordDict)
    
    def dp(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for end in range(n+1):
            for start in range(0, end):
                if dp[start] and s[start:end] in words:
                    dp[end] = True
                    break
        return dp[-1]
        
    def bfs(self, s, wordDict):
        words = set(wordDict)
        q = collections.deque([0])
        visited = set()
        n = len(s)
        while q:
            start = q.popleft()
            if start not in visited:
                for end in range(start, n+1):
                    if s[start:end] in words:
                        q.append(end)
                        if end == n:
                            return True
                visited.add(start)
        return False 
    
    def backtrack(self, s, wordDict):
        memo = {}
        words = set(wordDict)
        def helper(s, start):
            if start == n:
                return True
            if start in memo:
                return memo[start]
            for end in range(start, n+1):
                if s[start:end] in words and helper(s, end):
                    memo[start] = True
                    return memo[start]
            
            memo[start] = False
            return memo[start]
        
        n = len(s)    
        return helper(s, 0)
