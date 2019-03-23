"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        i = 0
        
        name = list(name)
        name.reverse()
        
        while i < len(typed):
            
            if name == []:
                return True
            
            if typed[i] == name[-1]:
                name.pop()
        
            i += 1
            
        if name != []:
            return False
        
        return True
