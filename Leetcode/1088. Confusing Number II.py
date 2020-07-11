"""
1088. Confusing Number II
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def confusingNumberII(self, N: int) -> int:
        confusing = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        nums = 0
        
        def dfs(n, rotated, digit):
            nonlocal nums
            if n != rotated:
                nums += 1
            for d in confusing:
                num = n* 10 + d
                if num > N: return
                dfs(num, confusing[d]*digit + rotated, digit*10)
        
        for d in confusing:
            if d: dfs(d, confusing[d], 10)
        return nums
