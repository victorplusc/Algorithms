"""
304. Range Sum Query 2D - Immutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
# Time complexity: O(1) per query, O(N*M) pre-compuitation
# Space complexity: O(N*M)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        if not matrix or not matrix[0]: 
            return
        m = len(matrix[0])
        self.dp = [[0] * (m+1) for _ in range(n+1)]
        for y in range(n):
            for x in range(m):
                self.dp[y+1][x+1] = self.dp[y][x+1] + self.dp[y+1][x] + matrix[y][x] - self.dp[y][x]

    def sumRegion(self, y1: int, x1: int, y2: int, x2: int) -> int:
        return self.dp[y2+1][x2+1] - self.dp[y1][x2+1] - self.dp[y2+1][x1] + self.dp[y1][x1]

"""
Using m rows of 1D range sums:

# Time complexity: O(N) per query, O(N*M) pre-compuitation
# Space complexity: O(N*M)
def __init__(self, matrix: List[List[int]]):
    n = len(matrix)
    if not matrix or not matrix[0]: 
        return
    m = len(matrix[0])
    self.dp = [[0] * (m+1) for _ in range(n)]
    for y in range(n):
        for x in range(m):
            self.dp[y][x+1] = self.dp[y][x] + matrix[y][x]

def sumRegion(self, y1: int, x1: int, y2: int, x2: int) -> int:
    region_sum = 0
    for y in range(y1, y2+1):
        region_sum += self.dp[y][x2+1] - self.dp[y][x1]
    return region_sum
"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
