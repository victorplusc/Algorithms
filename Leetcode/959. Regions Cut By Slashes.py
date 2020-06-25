"""
959. Regions Cut By Slashes
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

Example 1:
Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:
Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:
Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:
Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:
Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

Note:
1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
# Time complexity: O(N**2)
# Space complexity: O(N**2)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        graph = [[0] * (3*n) for _ in range(3*n)]
        for y in range(n):
            for x in range(n):
                if grid[y][x] == "/": graph[y*3][x*3+2] = graph[y*3+1][x*3+1] = graph[y*3+2][x*3] = 1
                if grid[y][x] == "\\": graph[y*3][x*3] = graph[y*3+1][x*3+1] = graph[y*3+2][x*3+2] = 1
        
        regions = 0
        for y in range(len(graph)):
            for x in range(len(graph[0])):
                if graph[y][x] == 0:
                    regions += 1
                    self.dfs(graph, y, x)
        return regions
        
    def dfs(self, graph, y, x):
        if y >= 0 and x >= 0 and x < len(graph[0]) and y < len(graph) and graph[y][x] == 0:
            graph[y][x] = 1
            self.dfs(graph, y-1, x)
            self.dfs(graph, y+1, x)
            self.dfs(graph, y, x-1)
            self.dfs(graph, y, x+1)
