"""
140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
# Time complexity: O(2**N + N**2 + W)
# Space complexity: O(2**N + N**2 + W)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # return self.top_down(s, wordDict)
        return self.bottom_up(s, wordDict)
    
    def bottom_up(self, s, wordDict):
        if set(collections.Counter(s).keys()) > set(collections.Counter("".join(wordDict)).keys()):
            return []

        words = set(wordDict)
        dp = [[]] * (len(s)+1)
        dp[0] = [""]
        for end in range(1, len(s)+1):
            sublist = []
            for start in range(0, end):
                word = s[start:end]
                if word in words:
                    for subsentence in dp[start]:
                        sublist.append((subsentence+ " " + word).strip())
            dp[end] = sublist
        return dp[-1]

    def top_down(self, s, wordDict):
        words = set(wordDict)
        memo = collections.defaultdict(list)
        
        def helper(s):
            if not s:
                return [[]]
            
            if s in memo:
                return memo[s]
            
            for end in range(1, len(s)+1):
                word = s[:end]
                if word in words:
                    for subsentence in helper(s[end:]):
                        memo[s].append([word] + subsentence)
            return memo[s]
        helper(s)
        return [" ".join(sentence) for sentence in memo[s]]
