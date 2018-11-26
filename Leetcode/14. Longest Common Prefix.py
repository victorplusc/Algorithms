#14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

All given inputs are in lowercase letters a-z.
"""

def longestCommonPrefix(strs: "Array of Strings"):
    if strs == []: return ""

    shortest = strs[0]

    for word in strs:
        if len(word) < len(shortest): shortest = word

    for i in range(len(shortest)):
        char = word[i]
        for word in strs:
            if word[i] != char:
                return word[0:i]

    return shortest

#Time complexity: O(N*M), N is the length of the shortest string, M is the length of the list.
#Space complexity: O(1).
