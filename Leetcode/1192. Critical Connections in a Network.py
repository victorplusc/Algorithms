"""
1192. Critical Connections in a Network
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:
1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""
# Time complexity: O(E+V)
# Space complexity: O(E)
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
            
        sorted_connections = set()
        for connection in connections:
            sorted_connections.add(tuple(sorted(connection)))
        
        rank = [-2] * n
        
        def dfs(node, depth):
            if rank[node] >= 0:
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for nei in graph[node]:
                if rank[nei] == depth-1:
                    continue
                back_depth = dfs(nei, depth+1)
                if back_depth <= depth:
                    sorted_connections.discard(tuple(sorted((node, nei))))
                min_back_depth = min(min_back_depth, back_depth)
            rank[node] = n
            return min_back_depth
        
        dfs(0, 0)
        return list(sorted_connections)
