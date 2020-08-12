"""
119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
"""
# Time complexity: O(K**2)
# Space complexity: O(K)
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        curr = [1]
        for i in range(rowIndex):
            new = [1]
            for j in range(len(curr)-1):
                new.append(curr[j]+curr[j+1])
            new.append(1)
            curr = new
        
        return curr
