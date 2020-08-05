"""
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr, num = "", 0
        for c in s:
            if c == "[":
                stack.append((curr, num))
                curr, num = "", 0
            elif c == "]":
                prev_s, prev_num = stack.pop()
                curr = prev_s + prev_num*curr
            elif c.isdigit():
                num = num*10 + int(c)
            else:
                curr += c
        return curr
