"""
952. Largest Component Size by Common Factor
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example 1:
Input: [4,6,15,35]
Output: 4

Example 2:
Input: [20,50,9,63]
Output: 2

Example 3:
Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:
1 <= A.length <= 20000
1 <= A[i] <= 100000
"""
class DisjointSet:
    def __init__(self, N):
        self.p = list(range(N))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def primes_set(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n%i == 0:
                    return primes_set(n//i) | {i}
            return {n}
        
        n = len(A)
        uf = DisjointSet(n)
        primes = collections.defaultdict(list)
        for i, num in enumerate(A):
            curr_primes = primes_set(num)
            for q in curr_primes:
                primes[q].append(i)
                
        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                uf.union(indexes[i], indexes[i+1])
        return max(collections.Counter([uf.find(i) for i in range(n)]).values())
