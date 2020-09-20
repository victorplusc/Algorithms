"""
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
10 <= low <= high <= 10^9
"""
# Time complexity: O(1)
# Space complexity: O(1)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        n = 10
        nums = []
        
        for i in range(len(str(low)), len(str(high))+1):
            for start in range(n-i):
                num = int(sample[start:start+i])
                if low <= num <= high:
                    nums.append(num)
        return nums
