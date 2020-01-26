"""
819. Most Common Word
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Note:

1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        alphabet = {chr(ord('a')+i) for i in range(26)} | {chr(ord('A')+i) for i in range(26)}
        banned = set(banned)
        hashmap = {}
        temp = []
        for c in paragraph:
            if c not in alphabet:
                word = "".join(temp).lower()
                if word and word not in banned:
                    hashmap[word] = hashmap.get(word, 0) + 1
                temp = []
            else:
                temp.append(c)
        if temp:
            word = "".join(temp).lower()
            if word and word not in banned:
                hashmap[word] = hashmap.get(word, 0) + 1
        max_pair = [0, ""]
        for s in hashmap:
            if hashmap[s] > max_pair[0]:
                max_pair = [hashmap[s], s]
        return max_pair[1]        
