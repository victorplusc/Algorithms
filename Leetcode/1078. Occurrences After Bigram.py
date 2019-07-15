"""
1078. Occurrences After Bigram
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.
"""
# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        third_words = []
        words = text.split()
        for i, word in enumerate(words):
            if i < len(words)-2:
                if word == first and words[i+1] == second:
                    third_words.append(words[i+2])
        return third_words
