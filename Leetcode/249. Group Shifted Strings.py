"""
249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
# Time complexity: O(NK)
# Space complexity: O(N)
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        order = {chr(ord('a')+i):i for i in range(26)}
        group = collections.defaultdict(list)
        for word in strings:
            distances = []
            for i in range(len(word)-1):
                distance = 26 + order[word[i+1]] - order[word[i]]
                distance %= 26
                distances.append(distance)
            group[tuple(distances)].append(word)
        return group.values()
