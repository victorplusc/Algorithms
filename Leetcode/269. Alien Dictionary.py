"""
269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"

Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
# Time complexity: O(C)
# Space complexity: O(min(U**2, N))
class Solution(object):
    def alienOrder(self, words):
        order = {}
        indeg = {chr(i):0 for i in range(ord('a'), ord('a')+26)}
        
        for w in words:
            for c in w:
                order[c] = set()
                
        def compare_words(word1, word2):
            min_length = min(len(word1), len(word2))
            for i in range(min_length):

                if word1[i] != word2[i]:
                    if word2[i] not in order[word1[i]]:
                        order[word1[i]].add(word2[i])
                        indeg[word2[i]] += 1
                    break
                elif i == min_length-1 and len(word1) > len(word2):
                    return False
            return True
        
        for i in range(len(words)-1):
            if not compare_words(words[i], words[i+1]):
                return ""
            
        q = collections.deque([c for c in indeg if indeg[c] == 0 and c in order])
        alphabet = []
        
        while q:
            front = q.popleft()
            alphabet.append(front)
            for c in order[front]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    q.append(c)
                    
        return "".join(alphabet) if len(alphabet) == len(order) else ""
