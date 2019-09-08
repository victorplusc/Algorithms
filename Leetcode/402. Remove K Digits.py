"""
402. Remove K Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

import collections

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        deque = collections.deque()
        
        i = 0
        while i < len(num):
            while k > 0 and deque and deque[-1] > num[i]:
                deque.pop()
                k -= 1
            deque.append(num[i])
            i += 1

        # takes care of edge cases where all numbers are the same
        while k > 0:
            deque.pop()
            k -= 1
        
        # remove leading "0"s
        while deque and deque[0] == "0":
            deque.popleft()
        
        # the last element could be "" if there was only a 0 in the new string
        return "".join(list(deque)) or "0"
