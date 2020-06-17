"""
Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        n, m = len(board), len(board[0])
        
        borders = set()
        borders |= {(x, 0) for x in range(m)}
        borders |= {(x, n-1) for x in range(m)}
        borders |= {(0, y) for y in range(n)}
        borders |= {(m-1, y) for y in range(n)}

        for (x, y) in borders:
            self.dfs(board, y, x)
        
        for y in range(n):
            for x in range(m):
                if board[y][x] == "O": board[y][x] = "X"
                elif board[y][x] == "V": board[y][x] = "O"
        
    def dfs(self, board, y, x):
        if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]) or board[y][x] != "O":
            return
        
        board[y][x] = "V"
        self.dfs(board, y, x-1)
        self.dfs(board, y, x+1)
        self.dfs(board, y-1, x)
        self.dfs(board, y+1, x)
