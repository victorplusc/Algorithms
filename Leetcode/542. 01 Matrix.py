"""
542. 01 Matrix
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
 
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        return self.bfs(matrix)
        return self.dp(matrix)

    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def bfs(self, matrix):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        n, m = len(matrix), len(matrix[0])
        queue = collections.deque()
        
        output = [[-1]* m for _ in range(n)]
        
        for y in range(n):
            for x in range(m):
                if matrix[y][x] == 0:
                    output[y][x] = 0
                    queue.append([y, x])
        
        while queue:
            y, x = queue.popleft()
            for dy, dx in dirs:
                nei_y, nei_x = y+dy, x+dx
                if 0 <= nei_y < n and 0 <= nei_x < m and output[nei_y][nei_x] == -1:
                    output[nei_y][nei_x] = output[y][x] + 1
                    queue.append([nei_y, nei_x])
        return output

    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def dp(self, matrix):
        if not matrix: return []
        
        n, m = len(matrix), len(matrix[0])
        dp = [[float('inf')]* m for _ in range(n)]
        
        for y in range(n):
            for x in range(m):
                if matrix[y][x] == 0:
                    dp[y][x] = 0
                else:
                    if y > 0:
                        dp[y][x] = min(dp[y][x], dp[y-1][x] + 1)
                    if x > 0:
                        dp[y][x] = min(dp[y][x], dp[y][x-1] + 1)
                        
        for y in reversed(range(n)):
            for x in reversed(range(m)):
                if y < n-1:
                    dp[y][x] = min(dp[y][x], dp[y+1][x] + 1)
                if x < m-1:
                    dp[y][x] = min(dp[y][x], dp[y][x+1] + 1)
        
        return dp
