"""
1383. Maximum Performance of a Team
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72

Constraints:
1 <= <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
"""
"""
n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2

efficiency = [9, 7, 5, 4, 3, 2]
speed = [1, 5, 2, 10, 3, 8]

current = 42 (after first 2)
sum = 6
heap [1, 5]

if (speed[i]+sum-heap[0])*efficiency[i] > current: then push and pop, update current
"""
# Time complexity: O(N * (log N + log K))
# Space complexity: O(N+K)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        combined = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        performance = total_vel = 0

        for eff, vel in combined:
            if len(heap) > k-1:
                total_vel -= heapq.heappop(heap)
            
            heapq.heappush(heap, vel)
            total_vel += vel
            performance = max(total_vel*eff, performance)
        return performance%(10**9+7)
