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

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:set() for i in range(n)}
        indeg = {i:0     for i in range(n)}
        for course, req in set(tuple(relation) for relation in prerequisites):
            graph[course] |= {req}
            indeg[req] += 1
            
        queue  =  [i for i in range(n) if not indeg[i]]
        visits =  set(queue) 
        for node in queue:
            for neighbour in graph[node]:
                if neighbour in visits: 
                    return False
                indeg[neighbour] -= 1
                if not indeg[neighbour]:
                    visits.add(neighbour)
                    queue += neighbour,
        return len(visits) == n
        
        
        
        
        
        
        
        
        
        
        
        
        
        
