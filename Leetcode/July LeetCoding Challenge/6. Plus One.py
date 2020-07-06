"""
Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            digits[0] += 1
            if digits[0] > 9:
                return [1, 0]
            return digits

        digits = [0] + digits
        digits[-1] += 1
        for i in reversed(range(len(digits))):
            if digits[i] <= 9:
                break
            temp = digits[i] // 10
            digits[i] %= 10
            digits[i-1] += temp
        
        return digits if digits[0] else digits[1:]
