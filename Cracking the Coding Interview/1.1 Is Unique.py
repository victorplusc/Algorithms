#1.1 Is Unique
"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

def isUnique(s: "String"):
    charSet = set()
    for c in s:
        if c in charSet: return False
        charSet.add(c)
    return True

#Time Complexity: O(N)
#Space Complexity: O(N)
