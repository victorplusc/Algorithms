"""
323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2

Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
# Time complexity: O(N+M)
# Space complexity: O(N)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return self.bfs_method(n, edges)
        return self.dfs_method(n, edges)
    
    def bfs_method(self, n, edges):
        graph = collections.defaultdict(list)
        
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        visited = [0] * n
        components = 0
        q = collections.deque()
        for i in range(n):
            if visited[i] == 0:
                q.append(i)
                while q:
                    k = q.popleft()
                    visited[k] = 1
                    for node in graph[k]:
                        if visited[node] == 0:
                            q.append(node)
                components += 1
        return components
    
    def dfs_method(self, n, edges):
        def dfs(k):
            visited[k] = 1
            for node in graph[k]:
                if visited[node] == 0:
                    dfs(node)

        graph = collections.defaultdict(list)
        
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            
        visited = [0] * n
        components = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                components += 1
        return components
