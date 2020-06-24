"""
96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    def numTrees(self, n: int) -> int:
        return self.dp(n)
        return self.mathematical(n)
    
    # Time complexity: O(N**2)
    # Space complexity: O(N)
    def dp(self, n):
        G = [0] * (n+1)
        G[0] = G[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
                
        return G[n]
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def mathematical(self, n):
        C = 1
        for i in range(n):
            C = C * 2 * (2*i+1)//(i+2)
        return C
