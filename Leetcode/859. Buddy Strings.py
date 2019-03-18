"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        
        if A == B:
            a_set = set()
            for char in A:
                if char in a_set:
                    return True
                else:
                    a_set.add(char)
            return False
            
        diff_a = None
        diff_b = None
        
        for i in range(len(A)):
            
            if A[i] != B[i]:
                
                if diff_a == None:
                    diff_a = A[i]
                    diff_b = B[i]
                elif diff_a != None:
                    if diff_b != A[i] or diff_a != B[i]:
                        return False
        
        return True
