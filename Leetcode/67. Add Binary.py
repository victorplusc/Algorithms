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
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.compute_bits(a, b)
    
    # Time complexity: O(N+M)
    # Space complexity: O(max(N, M))
    def cast_to_int(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
    # Time complexity: O(max(N, M))
    # Space complexity: O(max(N, M))
    def compute_bits(self, a, b):
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        answer = []
        for i in range(n-1, -1, -1):
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
    
    # Time complexity: O(N+M)
    # Space complexity: O(max(N, M))
    def bit_manip(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
