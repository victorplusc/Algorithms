"""
264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:
1 is typically treated as an ugly number.
n does not exceed 1690.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        
        while n > 1:
            u2, u3, u5 = 2*nums[i2], 3*nums[i3], 5*nums[i5]
            u_min = min(u2, u3, u5)
            if u_min == u2:
                i2 += 1
            if u_min == u3:
                i3 += 1
            if u_min == u5:
                i5 += 1
            nums.append(u_min)
            n -= 1
        return nums[-1]
