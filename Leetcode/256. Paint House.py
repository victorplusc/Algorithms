"""
256. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # return self.recursive(costs)
        return self.memoized(costs)

    # Time complexity: O(2**N)
    # Space complexity: O(N)
    def recursive(self, costs):
        if not costs:
            return 0
        return min(self.helper(costs, 0, 0), self.helper(costs, 0, 1), self.helper(costs, 0, 2))
                                                                                     
    def helper(self, costs, n, color):
        total_cost = costs[n][color]
        if n == len(costs)-1:
            return total_cost
        elif color == 0:
            total_cost += min(self.helper(costs, n+1, 1), self.helper(costs, n+1, 2))
        elif color == 1:
            total_cost += min(self.helper(costs, n+1, 0), self.helper(costs, n+1, 2))
        else:
            total_cost += min(self.helper(costs, n+1, 0), self.helper(costs, n+1, 1))
        return total_cost
    
    # Time complexity: O(2**N)
    # Space complexity: O(N)
    def memoized(self, costs):
        if not costs:
            return 0
        memo = {}
        return min(self.helper2(costs, 0, 0, memo), self.helper2(costs, 0, 1, memo), self.helper2(costs, 0, 2, memo))
                                                                                     
    def helper2(self, costs, n, color, memo):
        if (n, color) in memo:
            return memo[(n, color)]
        total_cost = costs[n][color]
        if n == len(costs)-1:
            return total_cost
        elif color == 0:
            total_cost += min(self.helper2(costs, n+1, 1, memo), self.helper2(costs, n+1, 2, memo))
        elif color == 1:
            total_cost += min(self.helper2(costs, n+1, 0, memo), self.helper2(costs, n+1, 2, memo))
        else:
            total_cost += min(self.helper2(costs, n+1, 0, memo), self.helper2(costs, n+1, 1, memo))
        memo[(n, color)] = total_cost
        return total_cost
