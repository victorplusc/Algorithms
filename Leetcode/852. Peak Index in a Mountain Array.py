#852. Peak Index in a Mountain Array

"""Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(A) - 1
        while left < right:
            mid = (left+right)//2
            if A[mid] < A[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
