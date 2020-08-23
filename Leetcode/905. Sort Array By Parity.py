# 905. Sort Array By Parity
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        i, j = 0, len(A)-1
        while i < j:
            if A[i] % 2 and not A[j] % 2:
                A[i], A[j] = A[j], A[i]
            
            if A[i] % 2 == 0: i += 1
            if A[j]%2 == 1: j -= 1
        return A
