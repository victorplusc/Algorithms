"""
1182. Shortest Distance to Target Color
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.

Constraints:
1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
"""
# Time complexity: O(Q log N + N)
# Space complexity: O(N)
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_indices = collections.defaultdict(list)
        for i, c in enumerate(colors):
            color_indices[c].append(i)
        
        def binary_search(indices, target):
            left, right = 0, len(indices)-1
            while left <= right:
                mid = (left+right)//2
                if indices[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            left_dist, right_dist = float('inf'), float('inf')
            if left < len(indices):
                left_dist = abs(indices[left] - target)
            if right >= 0:
                right_dist = abs(indices[right] - target)
            
            return min(left_dist, right_dist)
            
        output = []
        for i, c in queries:
            if colors[i] == c:
                output.append(0)
                continue
            dist = binary_search(color_indices[c], i)
            if dist == float('inf'): dist = -1
            output.append(dist)
        return output
