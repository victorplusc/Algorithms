"""
787. Cheapest Flights Within K Stops
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Note:
The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        return self.dijkstras(n, flights, src, dst, K)
        return self.bfs(n, flights, src, dst, K)
        return self.bellman_ford(n, flights, src, dst, K)
        
    # Time complexity: O(E + V log V)
    # Space complexity: O(E+V)
    def dijkstras(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, cost in flights:
            f[a][b] = cost
        heap = [(0, src, k+1)]
        while heap:
            cost, i, k = heapq.heappop(heap)
            if i == dst:
                return cost
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (cost + f[i][j], j, k-1))
        return -1
    
    # Time complexity: O(V+E)
    # Space complexity: O(E)
    def bfs(self, n, flights, src, dst, k):
        graph = collections.defaultdict(dict)
        q = collections.deque()
        min_price = float('inf')
        
        for u, v, cost in flights:
            graph[u][v] = cost

        q.append((0, src, 0))
        while q:
            stops, city, price = q.popleft()
            if city == dst:
                min_price = min(min_price, price)
                continue
            if stops <= k and price <= min_price:
                for nei in graph[city]:
                    q.append((stops+1, nei, graph[city][nei] + price))
        return min_price if min_price != float('inf') else -1
        
    # Time complexity: O(V**2 + E)
    # Space complexity: O(V)
    def bellman_ford(self, n, flights, src, dst, k):
        costs = [float('inf') for _ in range(n)]
        costs[src] = 0
        for _ in range(k+1):
            copy = costs[:]
            for u, v, cost in flights:
                copy[v] = min(copy[v], costs[u] + cost)
            costs = copy
        return -1 if costs[dst] == float('inf') else costs[dst]
