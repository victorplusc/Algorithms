# 896. Monotonic Array

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        is_monotone_inc = True
        is_monotone_dec = True
        
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                is_monotone_dec = False
            if A[i] > A[i+1]:
                is_monotone_inc = False
        
        return is_monotone_inc or is_monotone_dec

# Time complexity: O(N)
# Space complexity: O(1)
