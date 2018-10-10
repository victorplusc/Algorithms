"""
Given a string S and a character C, return an array of integers
representing the shortest distancefrom the character C in the string.
"""
#Example:
    #Input: S = "loveleetcode", C = 'e'
    #Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

"""
> S string length is in [1, 10000].
> C is a single character, and guaranteed to be in string S.
> All letters in S and C are lowercase.
"""

"""
I could find all indices of character C, then for each index I shift through of
S, find the minimal difference and place that difference in the array
"""

def shortestToChar(S: "String", C: "character"):
    distances = []
    locations = []
    for i in range(len(S)):
        if S[i] == C:
            locations.append(i)
    for j in range(len(S)):
        if S[j] == C:
            distances.append(0)
        else:
            distances.append(minimalDifferences(j, locations))
    return distances

def minimalDifferences(index: "integer", l: "list of numbers"):
    minimal = 10000
    for num in l:
        if abs(num-index) < minimal:
            minimal = abs(num-index)
    return minimal
