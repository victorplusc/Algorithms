"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # return self.top_down(coins, amount)
        return self.bottom_up(coins, amount)
    
    # Time complexity: O(S * n), where S is the amount, and n are the number of coins
    # Time complexity: O(S), amount of change we need for the memoization table
    def top_down(self, coins, amount):
        if amount < 1:
            return 0
        return self.helper(coins, amount, {})
        
    def helper(self, coins, rem, count):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if rem in count and count[rem] != 0:
            return count[rem]
        lowest = float('inf')
        for coin in coins:
            res = self.helper(coins, rem - coin, count)
            if 0 <= res < lowest:
                lowest = 1 + res
        count[rem] = -1 if lowest == float('inf') else lowest
        return count[rem]
    
    # Time complexity: O(S * n), where S is the amount, and n are the number of coins
    # Time complexity: O(S), amount of change we need for the dp table
    def bottom_up(self, coins, amount):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
