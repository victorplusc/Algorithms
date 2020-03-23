"""
365. Water and Jug Problem
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
 
Example 1: (From the famous "Die Hard" example)
Input: x = 3, y = 5, z = 4
Output: True

Example 2:
Input: x = 2, y = 6, z = 5
Output: False
"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # return self.bfs(x, y, z)
        return self.math_approach(x, y, z)
    
    # Time complexity: O(XY)
    # Space complexity: O(1)
    def bfs(self, x, y, z):
        if x+y < z:
            return False
        stack = [(0, 0)]
        visited = set((0, 0))
        while stack:
            a, b = stack.pop()
            if a+b == z:
                return True
            states = set()
            states.add((x, b))
            states.add((a, y))
            states.add((0, b))
            states.add((a, 0))
            states.add((min(x, b+a), 0 if b < x-a else b-(x-a)))
            states.add((0 if a+b < y else a-(y-b), min(b+a, y)))
            
            for state in states:
                if state in visited: continue
                stack.append(state)
                visited.add(state)
        return False
    
    # Time complexity: O(log N)
    # Space complexity: O(1)
    def math_approach(self, x, y, z):
        if x+y < z:
            return False
        if x == z or y == z or x+y == z:
            return True
        return z%self.GCD(x, y) == 0
        
    def GCD(self, a, b):
        while (b != 0):
            temp = b
            b = a%b
            a = temp
        return a
