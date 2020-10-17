"""
317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
             
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
"""
Traverse the matrix. For each building, use BFS to compute the shortest distance from each '0' to
this building. After we do this for all the buildings, we can get the sum of shortest distance
from every '0' to all reachable buildings. This value is stored
in 'distance[][]'. For example, if grid[2][2] == 0, distance[2][2] is the sum of shortest distance from this block to all reachable buildings.
"""
"""
Example:
input = [
    [1, 0, 0, 0, 0]
    [0, 0, 0, 2, 0]
    [0, 0, 1 ,0, 1]
]

distance = [
    [0, 9, 8, 9, 10]
    [11, 10, 9, 0, 11]
    [12, 11, 0, 2, 0]
]

reachable = [
    [0, 3, 3, 3, 3]
    [3, 3, 3, 0, 3]
    [3, 3, 0, 2, 0]
]

returns 8
"""
# Time complexity: O(#1s*#0s) ~O(N**2M**2)
# Space complexity: O(N*M)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        n, m = len(grid), len(grid[0])
        distance = [[0] * m for _ in range(n)]
        reachable = [[0] * m for _ in range(n)]
        buildings = 0
        
        def bfs(y, x):
            q = collections.deque([(y, x)])
            visited = set()
            depth = 1
            while q:
                size = len(q)
                for i in range(size):
                    curr_y, curr_x = q.popleft()

                    for dy, dx in dirs:
                        new_y = curr_y+dy
                        new_x = curr_x+dx

                        if new_y >= 0 and new_y < n and new_x >= 0 and new_x < m \
                        and grid[new_y][new_x] == 0 and (new_y, new_x) not in visited:
                            distance[new_y][new_x] += depth
                            reachable[new_y][new_x] += 1
                            visited.add((new_y, new_x))
                            q.append((new_y, new_x))
                depth += 1
        
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    buildings += 1
                    bfs(y, x)
                    
        shortest = float('inf')
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 0 and reachable[y][x] == buildings:
                    shortest = min(shortest, distance[y][x])
        
        return shortest if shortest != float('inf') else -1
