"""
59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

# Time complexity: O(N*N)
# Space complexity: O(1), no extra space

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        matrix = [[None for i in range(n)] for j in range(n)]    
        layer = 0
        count = 1
        
        while count <= n*n:
            for i in range(layer, len(matrix[0]) - layer):
                if not matrix[layer][i]:
                    matrix[layer][i] = count
                    count += 1

            for i in range(layer+1, len(matrix) - layer):
                if not matrix[i][-1-layer]:
                    matrix[i][-1-layer] = count
                    count += 1

            for i in range(layer+1, len(matrix[0]) - layer):
                if not matrix[-1-layer][-1-i]:
                    matrix[-1-layer][-1-i] = count
                    count += 1

            for i in range(layer+1, len(matrix) - layer - 1):
                if not matrix[-1-i][layer]:
                    matrix[-1-i][layer] = count
                    count += 1

            layer += 1
        
        return matrix
