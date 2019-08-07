"""
977. Squares of a Sorted Array
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        last_negative_index = -1

        for i, val in enumerate(A):
            if val < 0:
                last_negative_index = i
            A[i] *= val
        
        if len(A) == 1:
            return A
        
        merged = []
        
        if last_negative_index != -1:
            i = last_negative_index
            j = last_negative_index+1
            
            while i >= 0 and j < len(A):
                
                if A[i] < A[j]:
                    merged.append(A[i])
                    i -= 1
                else:
                    merged.append(A[j])
                    j += 1
            
            if i >= 0:
                for k in range(len(A[:i+1])):
                    merged.append(A[i-k])
                    
                    
            if j < len(A):
                for k in range(len(A[j:])):
                    merged.append(A[j+k])
            
            return merged
        
        return A
    
