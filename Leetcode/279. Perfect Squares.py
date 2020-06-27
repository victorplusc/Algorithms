"""
279. Perfect Squares
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
class Solution:
    def numSquares(self, n: int) -> int:
        # return self.dp(n)
        return self.bfs(n)
    
    # Time complexity: O(N**H/2)
    # Space complexity: O(sqrt(N)**H)
    def bfs(self, n):
        squares = [i**2 for i in range(int(math.sqrt(n)+1))]
        level = 0
        q = {n}
        while q:
            level += 1
            next_q = set()
            for remainder in q:
                for sq in squares:
                    if remainder == sq:
                        return level
                    elif remainder < sq:
                        break
                    else:
                        next_q.add(remainder - sq)
            q, next_q = next_q, q
        return level
    
    # Time complexity: O(N*sqrt(N))
    # Space complexity: O(N)
    def dp(self, n):
        squares = [i**2 for i in range(int(math.sqrt(n)+1))]
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for x in range(1, n+1):
            for sq in squares:
                if x < sq:
                    break
                dp[x] = min(dp[x], dp[x-sq]+1)
        return dp[-1]
