"""
Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binaryX = list(bin(x))[2:len(bin(x))]
        binaryY = list(bin(y))[2:len(bin(y))]

        lenDiff = len(binaryX) - len(binaryY)

        if lenDiff < 0:
            binaryX = ['0']*abs(lenDiff) + binaryX
        elif lenDiff > 0:
            binaryY = ['0']*lenDiff + binaryY

        distance = 0
        for i in range(len(binaryX)):
            if binaryX[i] != binaryY[i]:
                distance += 1

        return distance
