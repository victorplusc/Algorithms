"""
309. Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        
        n = len(prices)
        rest = [0]*n
        held = [0]*n
        sold = [0]*n
        
        rest[0] = 0
        held[0] = -prices[0]
        sold[0] = float('-inf')
        
        for i in range(1, n):
            rest[i] = max(rest[i-1], sold[i-1])
            held[i] = max(held[i-1], rest[i-1]-prices[i])
            sold[i] = held[i-1] + prices[i]

        return max(rest[-1], sold[-1])
