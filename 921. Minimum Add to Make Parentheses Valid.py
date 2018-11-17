"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

"""

def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        excessClosing = 0
        numOpen = 0
        
        for bracket in S:
            
            if bracket == "(":
                numOpen += 1
            elif bracket == ")" and numOpen != 0:
                numOpen -= 1
            else:
                excessClosing += 1
        
        return excessClosing + numOpen
