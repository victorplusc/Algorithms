"""
1197. Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:
|x| + |y| <= 300
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.bidir_bfs(x, y)
        return self.dfs(x, y)
    
    def dfs(self, x, y):
        base_cases = {(0, 0): 0, (1, 0): 3, (0, 1): 3, (1, 1): 2}
        def closure(x, y):
            if (x, y) in base_cases: return base_cases[(x, y)]
            moves = min(closure(abs(x-1), abs(y-2)), closure(abs(x-2), abs(y-1))) + 1
            base_cases[(x, y)] = moves
            return moves
        return closure(abs(x), abs(y))

    def bidir_bfs(self, x, y):
        def find_valid_moves(x, y):
            moves = []
            for i in [2, -2]:
                for j in [1, -1]:
                    moves.append((x+i, y+j))
                    moves.append((x+j, y+i))
            return moves
        
        def visit_node(q, visited, others_visited):
            a, b = q.popleft()
            for i, j in find_valid_moves(a, b):
                if (i, j) in others_visited:
                    return visited[(a, b)] + others_visited[(i, j)] + 1
                if (i, j) not in visited and -2 <= a <= abs(x)+2 and -2 <= b <= abs(y)+2:
                    visited[(i, j)] = visited[(a, b)] + 1
                    q.append((i, j))
                    
        if not x and not y:
            return 0
        x, y = abs(x), abs(y)
        q_start = collections.deque([(0, 0)])
        q_end = collections.deque([(x, y)])
        
        start_visited = {(0, 0): 0}
        end_visited = {(x, y): 0}
        
        while q_start and q_end:
            
            moves = visit_node(q_start, start_visited, end_visited)
            if moves:
                return moves
            moves = visit_node(q_end, end_visited, start_visited)
            if moves:
                return moves
