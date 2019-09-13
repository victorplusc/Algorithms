"""
243. Shortest Word Distance
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_ptr = word2_ptr = -1
        shortest = len(words)
        
        for i, word in enumerate(words):
            if word == word1:
                word1_ptr = i
            elif word == word2:
                word2_ptr = i
            
            if word1_ptr != -1 and word2_ptr != -1:
                shortest = min(abs(word1_ptr - word2_ptr), shortest)
                    
        return shortest

    
# Time complexity: O(N)
# Space complexity: O(N)
#     def shortestDistance(self, words, word1, word2):
#         """
#         :type words: List[str]
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         d = {}
        
#         for i, word in enumerate(words):
#             d[word] = d[word] | {i} if word in d else {i}
        
#         shortest = len(words)
#         for i in d[word1]:
#             for j in d[word2]:
#                 if abs(i-j) < shortest:
#                     shortest = abs(i-j)
                    
#         return shortest
