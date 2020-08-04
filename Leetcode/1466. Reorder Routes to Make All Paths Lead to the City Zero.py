"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:
2 <= n <= 5 * 10^4
connections.length == n-1
connections[i].length == 2
0 <= connections[i][0], connections[i][1] <= n-1
connections[i][0] != connections[i][1]
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # return self.dfs(n, connections)
        return self.bfs(n, connections)
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def bfs(self, n, connections):
        graph = collections.defaultdict(list)
        
        for p, q in connections:
            graph[p].append((q, 1))
            graph[q].append((p, 0))
        
        visited = set()
        changes = 0
        q = collections.deque([0])
        while q:
            front = q.popleft()
            visited.add(front)
            for nei, cost in graph[front]:
                if nei in visited: continue
                changes += cost
                q.append(nei)
        return changes
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def dfs(self, n, connections):
        graph = collections.defaultdict(list)
        
        roads = set()
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
            roads.add((p, q))
        
        visited = set()
        changes = 0 
        def dfs(node, parent):
            nonlocal changes
            visited.add(node)
            if (parent, node) in roads:
                changes += 1
            for nei in graph[node]:
                if nei in visited or nei == node: 
                    continue
    
                dfs(nei, node)

        dfs(0, -1)
        return changes
