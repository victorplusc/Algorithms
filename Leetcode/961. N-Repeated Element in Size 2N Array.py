"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        for i in A:
            d[i] = d.get(i,0) + 1
        
        for j in d:
            if d[j] == len(A)//2:
                return j
                
# Time complexity: O(N)
# Space complexity: O(N)
