#1.4 Palindrome Permutation
"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to dictionary words.
"""

def isPalindromePerm(s: "String"):
    odd = 0
    sCount = dict()
    
    for char in s:
        sCount[char] = sCount.get(char,0) + 1

    for char in sCount:
        if sCount[char]%2 != 0:
            odd+=1
            if len(s)%2 == 0 or odd > 1: return False

    return True

#Time Complexity: O(N)
#Space Complexity: O(N)
