# ### Phone Number / Digits-To-Letters
# 
# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 0 and 1 do not map to any letters.
# 
# Python:
# mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# Java:
# {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
#   0   1      2      3      4      5      6       7      8       9
# 
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]

"""
digits = "2345"
            ^
-> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
-> for each c in "ghi":
    -> ["ad+c","ae+c","af+c","bd+c","be+c","bf+c","cd+c","ce+c","cf+c"]


Algorithm:
1. Idea is to iterate over each digit
2. We keep a current list of "progress", partial list of representations
3. At each step, we iterate over mapping[digit]
4. Iterate over every element in our list of representations that are of length == i+1
5. We are done after these steps

T: ~O(3^N), assuming no 4 digit choices
S: ~O(3^N)
"""
# mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
def digits_to_letters(digits, mapping):
    if not digits:
        return []
    
    representations = [[c] for c in mapping[digits[0]]]
    # representations = ["a", "b", "c"]
    for i in range(1, len(digits)):
        current = []
        for c in mapping[digits[i]]:
            for j in range(len(representations)):
                current.append(representations[j]+[c])
        representations = current
    
    return ["".join(combo) for combo in representations]

print(digits_to_letters("23", mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}))
print(digits_to_letters("9", mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}))
print(digits_to_letters("293", mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}))


# mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
import itertools
def digits_to_letters2(digits, mapping):
    if not digits:
        return []
    
    return list("".join(list(combo)) for combo in itertools.product(*[list(mapping[d]) for d in digits]))
