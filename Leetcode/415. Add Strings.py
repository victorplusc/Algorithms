"""
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# Time complexity: O(N+M)
# Space complexity: O(max(N,M))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m, z = len(num1), len(num2), ord("0")
        added = []
        carry = 0
        i, j = n-1, m-1
        while i >= 0 or j >= 0 or carry == 1:
            x = ord(num1[i]) - z if i >= 0 else 0
            y = ord(num2[j]) - z if j >= 0 else 0
            added.append((x + y + carry)%10)
            carry = (x + y + carry) // 10
            i -= 1
            j -= 1
        return "".join(str(v) for v in added[::-1])
