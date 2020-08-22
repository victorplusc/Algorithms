class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        parityArray = [i for i in A if i%2==0]
        
        for i in A:
            if i%2 != 0:
                parityArray.append(i)
        
        return parityArray
