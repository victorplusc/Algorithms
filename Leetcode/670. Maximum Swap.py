"""
670. Maximum Swap
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Note:
The given number is in the range [0, 108]
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        nums = [str(i) for i in range(9, 0, -1)]

        mapping = collections.defaultdict()
        for i, val in enumerate(digits):
            mapping[val] = i
        
        for i, val in enumerate(digits):
            for n in nums:
                if n <= val: 
                    break
                    
                if n in mapping and mapping[n] > i:
                    digits[i], digits[mapping[n]] = digits[mapping[n]], digits[i]
                    return int("".join(digits))
        
        return num
