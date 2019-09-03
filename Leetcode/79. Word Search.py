"""
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# Time complexity: O(M*N*4**L), MxN board, L word length
# Space complexity: O(4**L)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.dfs(board, y, x, word, 0):
                    return True
        return False
    
    def dfs(self, board, y, x, word, index):
        if y >= len(board) or x >= len(board[0]) or y < 0 or x < 0 or board[y][x] != word[index]:
            return False
        if index == len(word)-1:
            return True
        board[y][x] = "*"
        exists = \
            self.dfs(board, y+1, x, word, index+1) or \
            self.dfs(board, y-1, x, word, index+1) or \
            self.dfs(board, y, x+1, word, index+1) or \
            self.dfs(board, y, x-1, word, index+1) 
        board[y][x] = word[index]
        return exists
