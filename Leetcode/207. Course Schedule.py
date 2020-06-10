"""
207. Course Schedule
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
# Time complexity: O(V+E)
# Space complexity: O(V+E)
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visits = [0 for _ in range(n)]
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for i in range(n):
            if not self.dfs(i, graph, visits):
                return False
        return True
    
    def dfs(self, i, graph, visits):
        if visits[i] == -1:
            return False
        if visits[i] == 1:
            return True
        visits[i] = -1
        for j in graph[i]:
            if not self.dfs(j, graph, visits):
                return False
        visits[i] = 1
        return True
        
        
# ============================================================================

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        indeg = {i:0 for i in range(n)}
        
        total_deps = 0
        for course, req in prerequisites:
            graph[req].append(course)
            indeg[course] += 1
            total_deps += 1
        
        non_dep = [node for node in graph if indeg[node] == 0]
        visited = 0
        
        while non_dep:
            req = non_dep.pop()
            for course in graph[req]:
                visited += 1
                indeg[course] -= 1
                if indeg[course] == 0:
                    non_dep.append(course)
        return visited == total_deps
