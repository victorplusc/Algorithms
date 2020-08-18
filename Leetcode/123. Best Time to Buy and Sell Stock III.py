"""
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
             
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
             
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        left_min = prices[0]
        right_max = prices[-1]
        
        n = len(prices)
        left_profits = [0]*n
        right_profits = [0]*(n+1)
        
        for i in range(1, n):
            left_profits[i] = max(left_profits[i-1], prices[i]-left_min)
            left_min = min(left_min, prices[i])
            
            j = n-1-i
            right_profits[j] = max(right_profits[j+1], right_max-prices[j])
            right_max = max(right_max, prices[j])
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])
        
        return max_profit
