class Solution:
    def isPalindrome(self, x):
        
        if x < 0 or (x%10 == 0 and x > 9):
            return False
        
        if x < 10:
            return True
        
        xStr = str(x)
        length = len(xStr)
        
        for i in range(length//2):
            if xStr[i] != xStr[length-i-1]:
                return False
            
        return True
