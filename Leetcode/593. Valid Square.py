"""
593. Valid Square
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""
# Time complexity: O(1)
# Space complexity: O(1)
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def get_distance(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        
        points = [p1, p2, p3, p4]
        
        distances = collections.Counter()
        for i in range(4):
            for j in range(i+1, 4):
                distances[get_distance(points[i], points[j])] += 1

        return len(distances.values()) == 2 and 4 in distances.values() and 2 in distances.values()
