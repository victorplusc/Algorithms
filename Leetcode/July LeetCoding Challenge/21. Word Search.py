"""
Word Search
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
        n, m = len(board), len(board[0])
        def dfs(y, x, idx):
            if y >= n or x >= m or y < 0 or x < 0 or board[y][x] != word[idx]:
                return False
            if idx == len(word)-1:
                return True
            board[y][x] = "*"
            exists = \
                dfs(y-1, x, idx+1) or \
                dfs(y+1, x, idx+1) or \
                dfs(y, x-1, idx+1) or \
                dfs(y, x+1, idx+1)
            board[y][x] = word[idx]
            return exists
        
        for y in range(n):
            for x in range(m):
                if dfs(y, x, 0):
                    return True
        return False
    
