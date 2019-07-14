"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

# Time complexity: O(N*M), where N is the number of rows, and M is the width of each row. If dimension are constant, then the time complexity does not scale and is therefore constant.
# Space complexity: O(N*M)
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in board:
            for i, char in enumerate(row):
                if "R" == char:
                    rook_row = row
                    rook_col = i
                    break
                    
        vertical_layout = []
        for row in board:
            vertical_layout.append(row[rook_col])
        
        total_captures = self.captures(vertical_layout) + self.captures(rook_row)
        return total_captures
        
    def captures(self, row: List[List[str]]) -> int:
        new_row = [char for char in row if char != "."]
        captures = 0
        for i, char in enumerate(new_row):
            if char == "p" and i<len(new_row)-1 and new_row[i+1] == "R":
                captures += 1
            elif char == "R" and i<len(new_row)-1 and new_row[i+1] == "p":
                captures += 1
        return captures
