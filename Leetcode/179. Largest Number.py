"""
179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""
# Time complexity: O(N log N)
# Space complexity: O(N)
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        comparator = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        formatted = [str(i) for i in nums]
        formatted.sort(reverse=1, key=functools.cmp_to_key(comparator))
        return "".join(formatted) if formatted[0] != "0" else "0"
