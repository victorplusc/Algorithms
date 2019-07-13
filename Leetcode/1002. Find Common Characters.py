"""
1002. Find Common Characters
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""

# Time complexity: O(N*M), N being the number of items in A, and M being the length of each item
# Space complexity: O(N)
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        default_mapping = {}
        result = []
        
        for c in A[0]:
            default_mapping[c] = default_mapping.get(c,0)+1
        
        for i, word in enumerate(A[1:]):
            common_chars = {}
            temp = {}
            for c in word:
                temp[c] = temp.get(c, 0)+1
            for c in temp:
                if c in default_mapping:
                    common_chars[c] = min(default_mapping[c], temp[c])
            default_mapping = common_chars
        
        for c in default_mapping:
            for i in range(default_mapping[c]):
                result.append(c)
        
        return result
