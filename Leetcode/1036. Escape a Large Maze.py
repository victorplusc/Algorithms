"""
1036. Escape a Large Maze
In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.

Example 1:
Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: 
The target square is inaccessible starting from the source square, because we can't walk outside the grid.

Example 2:
Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: 
Because there are no blocked cells, it's possible to reach the target square.

Note:
0 <= blocked.length <= 200
blocked[i].length == 2
0 <= blocked[i][j] < 10^6
source.length == target.length == 2
0 <= source[i][j], target[i][j] < 10^6
source != target
"""
# Time complexity: O(N**2)
# Space complexity: O(N**2)
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}
        found = False
        def bfs(source, target):
            nonlocal found
            q, seen = collections.deque([source]), {tuple(source)}
            while q:
                x0, y0 = q.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = x0+dx, y0+dy
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target:
                            found = True
                            return True
                        q.append([x, y])
                        seen.add((x, y))
                if len(seen) == 20000: return True
        
        valid = bfs(source, target)
        if found: return True
        return valid and bfs(target, source)
