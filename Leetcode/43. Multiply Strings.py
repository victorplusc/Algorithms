"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# Time complexity: O(N*M)
# Space complexity: O(N+M)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        pos = [0] * (n+m)
        zero = ord("0")
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                curr = (ord(num1[i]) - zero) * (ord(num2[j]) - zero)
                p1 = i + j
                p2 = i + j + 1
                prev_sum = curr + pos[p2]
                pos[p1] += prev_sum//10
                pos[p2] = prev_sum%10
        for i, v in enumerate(pos):
            if v != 0:
                return "".join(str(s) for s in pos[i:])
        return "0"
