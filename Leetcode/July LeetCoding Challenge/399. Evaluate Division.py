"""
399. Evaluate Division
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
# Time complexity: O(N*Q)
# Space complexity: O(N)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        
        for nodes, value in zip(equations, values):
            first, second = nodes

            graph[first].append((second, value))
            graph[second].append((first, 1/value))
        
        def bfs(query):
            start, end = query
            
            if start not in graph or second not in graph:
                return -1
            
            q = collections.deque([(start, 1)])
            visited = {start}
            
            while q:
                front, curr_prod = q.popleft()
                if front == end:
                    return curr_prod
                for node, val in graph[front]:
                    if node not in visited:
                        new_prod = curr_prod*val
                        graph[start].append((node, new_prod))
                        graph[node].append((start, 1/new_prod))
                        visited.add(node)
                        q.append((node, new_prod))
            return -1
        return [bfs(query) for query in queries]
    
