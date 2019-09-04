"""
794. Valid Tic-Tac-Toe State
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
"""

# Time and Space complexity: O(1)
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        player_one = 'X'
        player_two = 'O'
        
        x_count = 0
        o_count = 0
        for row in board:
            x_count += row.count('X')
            o_count += row.count('O')

        if o_count not in {x_count-1, x_count}: return False
        
        if self.win(board, player_one) and x_count-1 != o_count: return False
        if self.win(board, player_two) and x_count != o_count: return False

        return True
    
    def win(self, board, player):
        for x in range(3):            
            if all(board[x][y] == player for y in range(3)):
                return True
            if all(board[y][x] == player for y in range(3)):
                return True
            
        diag = player == board[1][1] == board[0][0] == board[2][2]
        anti_diag = player == board[1][1] == board[0][2] == board[2][0]

        return diag or anti_diag
