"""
Given a 2D screen, location of a pixel in the screen and a color, replace color of the given pixel and all adjacent same colored pixels with the given color.

screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 2, 2, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 2, 2, 0},
               {1, 1, 1, 1, 1, 2, 1, 1},
               {1, 1, 1, 1, 1, 2, 2, 1},
               };
               
x = 4, y = 4, newColor = 3

Output:
                {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 3, 3, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 3, 3, 0},
               {1, 1, 1, 1, 1, 3, 1, 1},
               {1, 1, 1, 1, 1, 3, 3, 1},
               };

"""
"""
0. Record the value/color at screen[y][x]
1. DFS at the starting position screen[y][x], assumption left, right, up, down?
2. DFS will be composed of:
   i) check if screen[y][x] != original color, if not, then return
   ii) check if y and x are within bounds, so x >= 0, y >= 0, x < N, y < M, if not, then return
   iii) screen[y][x] = new_color
   iv) DFS(x-1, y), DFS(x+1, y), DFS(x, y-1), DFS(x, y+1)
3. return screen
"""
def fill_color(screen, x, y, new_color):
    M, N = len(screen), len(screen[0])
    original_color = screen[y][x]
    
    if original_color == new_color:
        return screen
    
    def DFS(x, y):
        if x < 0 or x >= N or y < 0 or y >= M or screen[y][x] != original_color:
            return
        screen[y][x] = new_color
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
    
    DFS(x, y)
    return screen

screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

# for row in screen:
#     print(row)
    
fill_color(screen, 4, 4, 3)

# for row in screen:
#     print(row)

"""
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 3, 3, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 3, 3, 0},
               {1, 1, 1, 1, 1, 3, 1, 1},
               {1, 1, 1, 1, 1, 3, 3, 1},
               };
x = 4, y = 4, newColor = 3

M = 7, N = 7
original_color = 2


"""


"""
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

grid = [[1,1,1,1,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
        
output: 1

grid = [[1,1,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]]

"""

"""
1. saving each coordinate for each island in a hash set - preprocess the coordinates, 
    island_1 = {(2, 1), (xi, yi)..} O(nxm)
    island_2 = {(3, 4), (xi, yi)..} O(nxm)
2. BFS (starting from island 1) O(nxm)
3. Steps for BFS: (right, left, up down)
    - have a visited hash set {}
    - queue elements should be as follows: (x, y, dist)
    - if current element is 1, check if it's in island 2, then return dist
    - otherwise (it's 0)
        - increment distance by 1
        - BFS again, add neighbors to queue in the format (nei, dist), if they've not been visited
"""
import collections
def island_distance(grid):
    """
    grid = [[1,1,1,1,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
    """
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
    
grid = [[1,1,0,0,0],
        [1,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,1],
        [0,0,0,1,1]]

print(island_distance(grid))
