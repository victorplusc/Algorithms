"""
165. Compare Version Numbers
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
"""

# Time complexity: O(max(N, M))
# Space complexity: O(max(N, M))
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = [int(i) for i in version1.split(".")]
        v2_list = [int(i) for i in version2.split(".")]
        v1_len = len(v1_list)
        v2_len = len(v2_list)
        
        longer_list = v1_list if v1_len > v2_len else v2_list
        shorter_list = v2_list if v1_len > v2_len else v1_list
        
        for _ in range(len(longer_list)-len(shorter_list)):
            shorter_list.append(0)
        
        for i in range(len(v1_list)):
            if v1_list[i] > v2_list[i]:
                return 1
            elif v1_list[i] < v2_list[i]:
                return -1
        
        return 0
