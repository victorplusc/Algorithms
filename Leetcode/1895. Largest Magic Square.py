"""
1895. Largest Magic Square
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

Example 1:
Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

Example 2:
Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 106
"""
# Time complexity: O(N*M*min(N*M)^2)
# Space complexity: O(N*M)
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        prefix_row = [[0]*(m+1) for _ in range(n)]
        prefix_col = [[0]*(n+1) for _ in range(m)]
        for y in range(n):
            for x in range(m):
                prefix_row[y][x+1] = prefix_row[y][x] + grid[y][x]
                prefix_col[x][y+1] = prefix_col[x][y] + grid[y][x]
        
        
        def valid_squares(k):
            for y in range(n-k+1):
                for x in range(m-k+1):
                    diag, anti_diag = 0, 0
                    for i in range(k):
                        diag += grid[y+i][x+i]
                        anti_diag += grid[y+i][x+k-1-i]
                    matched = diag == anti_diag
                    
                    if not matched:
                        continue
                        
                    dy, dx = y, x
                    while dy < y + k and matched:
                        matched = prefix_row[dy][x+k]-prefix_row[dy][x] == diag
                        dy += 1

                    while dx < x + k and matched:
                        matched = prefix_col[dx][y+k]-prefix_col[dx][y] == diag
                        dx += 1
                        
                    if matched:
                        return True
            return False
        for k in range(min(m, n), 1, -1):
            if valid_squares(k): return k
        return 1
       
