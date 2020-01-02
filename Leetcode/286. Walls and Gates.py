"""
286. Walls and Gates
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

import collections
class Solution:
    ## BFS
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        m = len(rooms)
        if m == 0: return
        n = len(rooms[0])
        queue = collections.deque()
        for y, row in enumerate(rooms):
            for x, val in enumerate(row):
                if val == 0:
                    queue.append((y, x))
        
        while queue:
            point = queue.popleft()
            x = point[1]
            y = point[0]
            for y_delta, x_delta in directions:
                r = y + y_delta
                c = x + x_delta
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != EMPTY:
                    continue
                rooms[r][c] = rooms[y][x] + 1
                queue.append((r, c))
    
    ## DFS
    # Time complexity: O(K*N*M), where K is the number of gates
    # Space complexity: O(N*M)
    def wallsAndGates2(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0: return
        n = len(rooms[0])
        for y, room in enumerate(rooms):
            for x, val in enumerate(room):
                if val == 0:
                    self.room_distance(rooms, y, x, m, n)


    def room_distance(self, rooms, y, x, m, n, d=0):
        if x < 0 or y < 0 or y >= m or x >= n or rooms[y][x] < d:
            return
        rooms[y][x] = d
        self.room_distance(rooms, y+1, x, m, n, d+1)
        self.room_distance(rooms, y-1, x, m, n, d+1)
        self.room_distance(rooms, y, x+1, m, n, d+1)
        self.room_distance(rooms, y, x-1, m, n, d+1)
