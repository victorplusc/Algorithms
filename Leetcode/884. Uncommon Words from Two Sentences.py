"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.
"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        tableA = {}
        for i in A.split():
            if i not in tableA:
                tableA[i] = 1
            else:
                tableA[i] += 1
        
        tableB = {}
        for i in B.split():
            if i not in tableB:
                tableB[i] = 1
            else:
                tableB[i] += 1
                
        uncommon = []
        
        for word in tableA:
            if tableA[word] == 1 and word not in tableB:
                uncommon.append(word)
        
        for word in tableB:
            if tableB[word] == 1 and word not in tableA:
                uncommon.append(word)
        
        return uncommon

# Time complexity: O(A + B)
# Space complexity: O(A + B)
