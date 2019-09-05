"""
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""

# Time complexity: O(N*M), where N is the size of s and M is the word length
#               <= O(M * N/M * M) = O(N*M)
# Space complexity: O(K), where K is the size of words
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        
        word_bag = {}
        for word in words:
            word_bag[word] = word_bag.get(word, 0) + 1
        
        num_words = len(words)
        word_len = len(words[0])
        total_len = word_len*num_words
        
        indices = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            
            for j in range(i, i+total_len, word_len):
                curr_word = s[j:j+word_len]
                if curr_word in word_bag:
                    seen[curr_word] = seen.get(curr_word, 0) + 1
                    if seen[curr_word] > word_bag[curr_word]:
                        break
                else:
                    break
            
            if seen == word_bag:
                indices.append(i)
        return indices
