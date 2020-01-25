"""
49. Group Anagrams
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
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.using_sorted_words(strs)
        return self.using_list_as_key(strs)
        return self.using_str_as_key(strs)
    
    # Time complexity: O(N*K)
    # Space complexity: O(N*K)
    def using_list_as_key(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        for word in strs:
            count = [0 for _ in range(26)]
            for c in word:
                count[ord(c)-ord('a')] += 1
            group[tuple(count)].append(word)
        return group.values()
    
    # Time complexity: O(NKlogK)
    # Space complexity: O(N*K)
    def using_str_as_key(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        for word in strs:
            count = {}
            for c in word:
                count[c] = count.get(c, 0) + 1
            group["".join(sorted(word))].append(word)
        return group.values()
    
    # Time complexity: O(NKlogK)
    # Space complexity: O(NK)
    def using_sorted_words(self, strs):
        group = collections.defaultdict(list)
        for word in strs:
            group["".join(sorted(word))].append(word)
        return group.values()
