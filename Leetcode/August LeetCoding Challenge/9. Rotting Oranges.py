"""
Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        rotten_locations = collections.deque()
        fresh_oranges = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    fresh_oranges += 1
                elif val == 2:
                    rotten_locations.append([y, x])
        if fresh_oranges == 0: return 0
        
        cycles = 0
        while rotten_locations:
            size = len(rotten_locations)
            for i in range(size):
                curr = rotten_locations.popleft()
                y = curr[0]
                x = curr[1]
                for dy, dx in directions:
                    r = y + dy
                    c = x + dx
                    if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0 or grid[r][c] == 2:
                        continue

                    grid[r][c] = 2
                    rotten_locations.append([r, c])
                    fresh_oranges -= 1

            cycles += 1
            if fresh_oranges == 0:
                return cycles

        return -1
                    
            
