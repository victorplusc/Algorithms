#1.2 Check Permuatation
"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

def checkPermutation(s1 : "String", s2 : "String"):
    if len(s1) != len(s2):
        return False
    
    sCount = dict()

    for char in s1:
        sCount[char] = sCount.get(char,0) + 1

    #if the character does not exist, its count becomes '-1'. All character counts should reach zero for both strings to be permutations of each other.
    for char in s2:
        sCount[char] = sCount.get(char,0) - 1
        if sCount[char] < 0: return False
    
    return True

#Time Complexity: O(N)
#Space Complexity: O(N)
