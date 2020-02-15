"""
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
# Time complexity O(N!)
# Space complexity: O(N)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def could_place(row, col):
            return not (cols[col] + up_diag[row-col] + down_diag[row+col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            up_diag[row-col] = 1
            down_diag[row+col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            up_diag[row-col] = 0
            down_diag[row+col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append("." * col + "Q" + "." * (n - col - 1))
            output.append(solution)
        
        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)
        
        cols = [0] * n
        down_diag = [0] * (2*n -1)
        up_diag = [0] * (2*n - 1)
        queens = set()
        output = []
        backtrack()
        return output
