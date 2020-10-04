"""
/**
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
*/ 

s = "{)}{[)((]"

s = "(((((("
where # opening circular are == 0, then we know it's invalid

1) instantiate a stack
2) iterate over s

complements = {")" : "(", "}" : "{", "]" : "["}

if the character at s[i] is an opening bracket:
    append to the stack
else: # if s[i] is a closing bracket
    if not stack:
        return False
    #if s[i] is ")", then we want to check the top of the stack to see if it's "("
    if complements[s[i]] != stack[-1]:
        return False
    stack.pop()

return len(stack) == 0

s = "{)}{[)((]"
      ^
stack = ["{"]

s = "()(){[()]}"
            ^
stack = [{, [, (]
"""

def valid_parentheses(s):
    complements = {")" : "(", "}" : "{", "]" : "["}
    
    stack = []
    for c in s:
        if c not in complements:
            stack.append(c)
        else:
            if not stack or complements[c] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parentheses("{)}{[)((]"))
print(valid_parentheses("()(){[()]}"))
print(valid_parentheses("(((((((("))
print(valid_parentheses("]]]]]]]]"))
print(valid_parentheses("([)]"))

'''
Given an array of integers nums and an integer k, return the number of unique
k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] <= [nums[j]]
nums[j] - nums[i] == k


[1, 2, 3, 1, 3] k = 2
output: 1

'''
"""
search for 
nums[j] == k + nums[i]

1) instantiate a set()
2) add nums[i] into the set
3) iterate over the set and check for nums[i] + k in the set, if so, increment total counter
4) return
"""

import collections
def k_diff_pairs(A, k):
    counter = collections.Counter(A)
    total = 0
    for num in counter:
        if k > 0 and num+k in counter:
            total += 1
        elif k == 0 and counter[num] > 1:
            total += 1
    return total

print(k_diff_pairs([1, 2, 3, 1, 3], 2))
print(k_diff_pairs([1, 2, 3, 4, 5], 1))
print(k_diff_pairs([1, 5, 3, 5, 5], 0))
