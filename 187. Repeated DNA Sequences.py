"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        occurrences = {}
        
        for i in range(len(s)-9):
            new = (s[i:i+10])
            
            if new not in occurrences:
                occurrences[new] = False
            else:
                occurrences[new] = True
            
        return ([i for i in occurrences if occurrences[i] == True])
