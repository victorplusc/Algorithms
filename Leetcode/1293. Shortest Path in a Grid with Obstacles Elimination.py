"""
1293. Shortest Path in a Grid with Obstacles Elimination
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        if k >= n+m-2:
            return n+m-2
        
        queue = collections.deque([[0, 0, k]])
        depth = 0
        seen = {(0, 0, k)}
        while queue:
            for i in range(len(queue)):
                x, y, r = queue.popleft()
                if (x, y) == (m-1, n-1):
                    return depth
                for dx, dy in directions:
                    new_x, new_y = x+dx, y+dy
                    if new_x >= m or new_x < 0 or new_y >= n or new_y < 0:
                        continue
                    
                    if grid[new_y][new_x] == 1:
                        if r > 0 and (new_x, new_y, r-1) not in seen:
                            queue.append([new_x, new_y,r-1])
                            seen.add((new_x, new_y, r-1))
                    elif (new_x, new_y, r) not in seen:
                        queue.append([new_x, new_y,r])
                        seen.add((new_x, new_y, r))
            depth += 1            
        return -1
