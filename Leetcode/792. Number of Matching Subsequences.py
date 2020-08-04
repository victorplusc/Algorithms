"""
792. Number of Matching Subsequences
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example:
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:
All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
# Time complexity: O(N*M)
# Space complexity: O(M)
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)
        
        for c in S:
            words_expecting_c = word_dict[c]
            word_dict[c] = []
            for word in words_expecting_c:
                if len(word) == 1:
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        return count
