"""
258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution:
    def addDigits(self, num: int) -> int:
        # return self.iterative(num)
        return self.equation(num)

    # Time complexity: O(N)
    # Space complexity: O(1)
    def iterative(self, num):
        while num > 9:
            temp = 0
            while num > 0:
                temp += num%10
                num //= 10
            num = temp
        return num
    
    # Time complexity: O(1)
    # Space complexity: O(1)
    def equation(self, num):
        if not num:
            return 0
        return 1 + (num-1)%9
