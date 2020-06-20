# 1) Explain what pointers are.
# 2) Explain differences between linked lists and arrays (dynamic memory allocation, time complexity, etc.).
"""
Reverse a string.
"""
# Time complexity: O(N)
# Space complexity: O(N)
def reverse_string(s):
    new_s = list(s)
    
    for i in range(len(s)//2):
        new_s[i], new_s[~i] = new_s[~i], new_s[i]
    return "".join(new_s)
    
"""
Given an array of single numbers, return how many matching pairs exist. You will never be given more than two characters that are the same (this means one pair max of each character).

Example:
Input: [ 1, 2, 6, 7, 6, 7]
Expected Result: 2
"""
# Time complexity: O(N)
# Space complexity: O(N)
def find_matching_pairs(A):
    seen = set()
    pairs = 0
    
    for val in A:
        if val in seen:
            pairs += 1
        else:
            seen.add(val)
    return pairs
