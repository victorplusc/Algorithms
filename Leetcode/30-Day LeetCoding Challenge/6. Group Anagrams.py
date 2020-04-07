"""
Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
# Time complexity: O(N*K)
# Space complexity: O(N*K)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            combination = [0] * 26
            for c in s:
                combination[ord("a") - ord(c)] += 1
            groups[tuple(combination)].append(s)
        return groups.values()
