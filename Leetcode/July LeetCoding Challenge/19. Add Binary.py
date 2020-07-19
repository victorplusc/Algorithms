"""
67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
# Time complexity: O(max(N, M))
# Space complexity: O(max(N, M))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = "0" * (n-len(a)) + a
        b = "0" * (n-len(b)) + b

        carry = 0
        answer = []
        for i in reversed(range(n)):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            
            if carry%2 == 1:
                answer.append("1")
            else:
                answer.append("0")
            carry //= 2
        if carry == 1:
            answer.append("1")
        answer.reverse()
        return "".join(answer)
