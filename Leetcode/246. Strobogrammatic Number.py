"""
246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        non_strobo = {"2","3","4","5","7"}
        spec_strobo = {"6":"9", "9":"6"}
        if len(num) == 1:
            if num in non_strobo | {"6", "9"}:
                return False
            return True
        
        for i in range(len(num)//2+1):
            if num[i] in non_strobo or num[-1-i] in non_strobo:
                return False
            elif num[i] in spec_strobo and num[-1-i] != spec_strobo[num[i]]:
                return False
            elif num[i] != num[-1-i] and num[i] not in spec_strobo and num[-1-i] not in spec_strobo:
                return False
            
        return True
