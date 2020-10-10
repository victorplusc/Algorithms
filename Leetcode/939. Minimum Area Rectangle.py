"""
939. Minimum Area Rectangle
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:
1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""
# Time complexity: O(N**2)
# Space complexity: O(N)
class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        mapping = collections.defaultdict(set)
        for x, y in points:
            mapping[x].add(y)

        min_area = float('inf')
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if x1 == x2 or y1 == y2:
                    continue
                if y2 in mapping[x1] and y1 in mapping[x2]:
                    min_area = min(min_area, abs(x2-x1)*abs(y2-y1))

        return min_area if min_area != float('inf') else 0
