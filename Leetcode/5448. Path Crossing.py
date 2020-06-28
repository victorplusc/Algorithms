"""
5448. Path Crossing
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
1 <= path.length <= 10^4
path will only consist of characters in {'N', 'S', 'E', 'W}
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x = y = 0
        for d in path:
            if d == "N":
                y += 1
            elif d == "S":
                y -= 1
            elif d == "E":
                x += 1
            elif d == "W":
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
