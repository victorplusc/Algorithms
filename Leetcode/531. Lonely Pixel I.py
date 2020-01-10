"""
531. Lonely Pixel I
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
"""
class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # return self.constant_space(picture)
       return self.linear_space(picture)
    
    def linear_space(self, picture):
        m = len(picture)
        if m == 0:
            return 0
        n = len(picture[0])
        
        vertical = [0 for _ in range(m)]
        horizontal = [0 for _ in range(n)]
        
        for y, row in enumerate(picture):
            for x, val in enumerate(row):
                if val == "B":
                    vertical[y] += 1
                    horizontal[x] += 1
        lonely = 0
        for y, row in enumerate(picture):
            for x, val in enumerate(row):
                if val == "B" and vertical[y] == 1 and horizontal[x] == 1:
                    lonely += 1
        return lonely

    # Time complexity: O(N)
    # Space complexity: O(1)
    def constant_space(self, picture):
        n = len(picture)
        if n == 0: return 0
        m = len(picture[0])
        
        first_row_count = 0
        for i, row in enumerate(picture):
            for j, val in enumerate(row):
                if val == "B":
                    if picture[0][j] < "Y" and picture[0][j] != "V":
                        picture[0][j] = chr(ord(picture[0][j])+1)
                    if i == 0:
                        first_row_count += 1
                    elif (picture[i][0] < "Y" and picture[i][0] != "V"):
                        picture[i][0] = chr(ord(picture[i][0])+1)
        count = 0
        for i, row in enumerate(picture):
            for j, val in enumerate(row):
                if picture[i][j] < "W" and (picture[0][j] == "C" or picture[0][j] == "X"):
                    if i == 0:
                        count += 1 if first_row_count == 1 else 0
                    elif picture[i][0] == "C" or picture[i][0] == "X":
                        count += 1
        return count
