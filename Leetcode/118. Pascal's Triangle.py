"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""
# Time complexity: O(N^2)
# Space complexity: O(N^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows == 1:
            return triangle
        
        triangle.append([1, 1])
        if numRows == 2:
            return triangle
            
        for i in range(numRows-2):
            new_row = [1]
            old_row = triangle[-1]
            for j in range(len(old_row)-1):
                new_row.append(old_row[j] + old_row[j+1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle
