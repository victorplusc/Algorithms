"""
973. K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
# Time complexity: O(N log K)
# Space complexity: O(N)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points
        
        heap = [(-self.modified_euclidean(points[i]), points[i]) for i in range(K)]
        heapq.heapify(heap)
        for i in range(K, len(points)):
            heapq.heappushpop(heap, (-self.modified_euclidean(points[i]), points[i]))
        return [point for d, point in heap]
    
    def modified_euclidean(self, point):
        x = point[0]
        y = point[1]
        return y**2+x**2
