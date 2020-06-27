"""
Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
# Time complexity: O(N**H/2)
# Space complexity: O(sqrt(N)**H)
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(sqrt(n)+1))]
        
        level = 0
        q = collections.deque([n])
        visited = set()
        while q:
            size = len(q)
            level += 1
            for i in range(size):
                remainder = q.popleft()
                for sq in squares:
                    if remainder < sq:
                        break
                    elif remainder == sq:
                        return level
                    elif remainder-sq not in visited:
                        q.append(remainder-sq)
                        visited.add(remainder-sq)
        return level
