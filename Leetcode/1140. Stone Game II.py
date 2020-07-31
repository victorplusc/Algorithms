"""
1140. Stone Game II
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""
# Time complexity: O(N**2)
# Space complexity: O(N**2)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if not piles: return 0
        n = len(piles)
        sums = [0] * n
        sums[-1] = piles[-1]
        for i in reversed(range(n-1)):
            sums[i] = sums[i+1] + piles[i]

        memo = {}
        def helper(i, M):
            if i == n: return 0
            if 2*M >= n-i:
                return sums[i]
            if (i, M) in memo: return memo[(i, M)]
            min_val = float('inf')
            for x in range(1, 2*M+1):
                min_val = min(min_val, helper(i+x, max(M, x)))
            memo[(i, M)] = sums[i] - min_val
            return memo[(i, M)]
        return helper(0, 1)
