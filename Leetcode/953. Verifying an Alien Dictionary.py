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
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {c:i for i, c in enumerate(order)}
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            diff = False
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if dictionary[word1[j]] > dictionary[word2[j]]:
                        return False
                    diff = True
                    break

            if not diff and len(word1) > len(word2): return False
                    
        return True
