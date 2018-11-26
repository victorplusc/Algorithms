#14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

All given inputs are in lowercase letters a-z.
"""

def longestCommonPrefix(strs: "Array of Strings"):
    prefix = []
    if strs != []:
        shortest = len(strs[0])
    else:
        return ""
    for word in strs:
        if len(word) < shortest: shortest = len(word)

    for i in range(shortest):
        char = word[i]
        for word in strs:
            if word[i] != char:
                return "".join(prefix)
        prefix.append(word[i])
        
    return "".join(prefix)

#Time complexity: O(N*M), N is the length of the shortest string, M is the length of the list.
#Space complexity: O(N), N is the length of the shortest string.
