# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        elif len(s) == 1:
            return True
        
        mapping_s = {}
        mapping_t = {}
        
        for i in range(len(s)):
            
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
            
            if t[i] not in mapping_t:
                mapping_t[t[i]] = s[i]
            
            if s[i] in mapping_s:
                if mapping_t[t[i]] != s[i]:
                    return False
                
            if t[i] in mapping_t:
                if mapping_s[s[i]] != t[i]:
                    return False
                
        return True
        
# Time complexity: O(N)
# Space complexity: O(N)
