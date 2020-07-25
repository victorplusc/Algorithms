"""
743. Network Delay Time
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""
# Time complexity: O(N**2 + E)
# Space complexity: O(N+E)
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        pq = [(0, K)]
        times = {}
        while pq:
            time, node = heapq.heappop(pq)
            if node in times: continue
            times[node] = time
            for v, w in graph[node]:
                heapq.heappush(pq, (time+w, v))
        return max(times.values()) if len(times) == N else -1
