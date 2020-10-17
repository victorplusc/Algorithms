"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Note:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""
# Time complexity: O(N*k), where N is the length of the input array, and k is the length of each word.
# Space complexity: O(1)
"""
Check for:
1. Different characters, check the order of the two characters
2. Proper lengths, i.e. if no differences occur, word1 should never be longer than word2

Algorithm:
1) Enumerate the order in a hashmap, higher value implies farther down in the alphabet
2) Iterate through the range of minimal length between two words
3) If word1[i] != word2[i]:
    i) if the word[i] in dict > word2[i] in dict, return False immediately
    ii) record a difference and break
4) If there is no difference and length of word1 > len(word2): False
5) the order of the two words is valid
6) repeat for all words
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {c:i for i, c in enumerate(order)}
        
        def valid_order(word1, word2):
            diff = False
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if dictionary[word1[i]] > dictionary[word2[i]]:
                        return False
                    diff = True
                    break
            if not diff and len(word1) > len(word2):
                return False
            return True
        
        return all(valid_order(words[i], words[i+1]) for i in range(len(words)-1))
