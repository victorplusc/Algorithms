"""
Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        elif len(coordinates) < 2:
            return False
        
        a, b = coordinates[0]
        c, d = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - a) * (d - b) != (y - b) * (c - a):
                return False
        return True
