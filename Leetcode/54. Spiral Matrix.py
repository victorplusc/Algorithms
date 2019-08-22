"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# Time complexity: O(N)
# Space complexity: O(1), no additional space required

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        numbers = []
        if matrix == []:
            return []
        
        size = len(matrix)*len(matrix[0])
        layer = 0
        while len(numbers) < size:
            
            for i in range(layer, len(matrix[0]) - layer):
                numbers.append(matrix[layer][i])
            
            for i in range(layer+1, len(matrix) - layer):
                numbers.append(matrix[i][-1-layer])
            
            for i in range(layer+1, len(matrix[0]) - layer):
                numbers.append(matrix[-1-layer][-1-i])
            
            for i in range(layer+1, len(matrix) - layer - 1):
                numbers.append(matrix[-1-i][layer])
            
            layer += 1
            
        return numbers[:size]
