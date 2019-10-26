"""
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
# Time complexity: O(N*M), where N is the length of the array and M is each word's length
# Space complexity: O(1), only 26 characters in the worst case
import collections
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = collections.Counter(chars)
        length_sum = 0
        for w in words:
            valid = True
            w_counts = collections.Counter(w)
            for c in w_counts:
                if c not in char_counts or char_counts[c] < w_counts[c]:
                    valid = False
                    break
            if valid: 
                length_sum += len(w)
        return length_sum
