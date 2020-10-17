"""
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:
Input: matrix = [], target = 0
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
# Time complexity: O(log N + log M)
# Space complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or matrix[0][0] > target:
            return False
        
        n, m = len(matrix), len(matrix[0])
        def bin_search_vertically():
            top = 0
            bottom = n-1
            while top <= bottom:
                mid = (top+bottom)//2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][0] > target:
                    bottom = mid - 1
                else:
                    top = mid + 1
            return -1
        
        y = bin_search_vertically()
        if y == -1:
            return False

        left = 0
        right = m-1
        while left <= right:
            mid = (left+right)//2
            if matrix[y][mid] == target:
                return True
            elif matrix[y][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
            
