"""
934. Shortest Bridge
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def preprocess(x, y, island):
            if x < 0 or x >= N or y < 0 or y >= M or grid[y][x] != 1 or (x, y) in island:
                return
            island.add((x, y))
            preprocess(x-1, y, island)
            preprocess(x+1, y, island)
            preprocess(x, y-1, island)
            preprocess(x, y+1, island)

        island_1 = set()
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1 and island_1 == set():
                    preprocess(x, y, island_1)
                    break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = {item for item in island_1}
        q = collections.deque([(x, y, -1) for x, y in island_1])
        while q:
            x, y, dist = q.popleft()
            if grid[y][x] == 1 and (x, y) not in island_1:
                return dist
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if (new_x, new_y) not in visited and new_x >= 0 and new_x < N and new_y >= 0 and new_y < M:
                    q.append((new_x, new_y, dist+1))
                    visited.add((new_x, new_y))
