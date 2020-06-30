"""
332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        return self.dfs(tickets)
        return self.backtracking(tickets)
    
    # Time complexity: O(E log E/V)
    # Space complexity: O(V + E)
    def dfs(self, tickets):
        graph = collections.defaultdict(list)
        
        for start, end in tickets:
            graph[start].append(end)
        
        for node in graph:
            graph[node].sort(reverse=True)
        
        itinerary = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
                
            itinerary.append(stack.pop())
            
        return itinerary[::-1]
    
    # Time complexity: O(E**d)
    # Space complexity: O(V + E)
    def backtracking(self, tickets):
        def bt(start, route):
            nonlocal itinerary
            if len(route) == n+1:
                itinerary = route
                return True
            for i, next_dest in enumerate(graph[start]):
                if not visited_bitmap[start][i]:
                    visited_bitmap[start][i] = True
                    new = bt(next_dest, route+[next_dest])
                    visited_bitmap[start][i] = False
                    if new:
                        return True
            return False
        
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        
        visited_bitmap = {}
        for start, locs in graph.items():
            locs.sort()
            visited_bitmap[start] = [False]*len(locs)
        
        n = len(tickets)
        itinerary = []
        route = ["JFK"]
        bt("JFK", route)
        return itinerary
