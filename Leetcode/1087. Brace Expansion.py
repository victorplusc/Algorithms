class Solution:
    def expand(self, S: str) -> List[str]:
        results = []
        
        char_count = 0
        inside_brackets = False
        bracket_index = {}
        new_str = []
        for i, c in enumerate(S):
            
            if c == "{":
                bracket_index[char_count] = []
                new_str.append("*")
                inside_brackets = True
            
            if not inside_brackets:
                char_count += 1
                new_str.append(c)
            
            if c == "}" and inside_brackets:
                char_count += 1
                inside_brackets = False
                
            if c not in {"{", "}", ","} and inside_brackets:
                bracket_index[char_count].append(c)
                
            
        #formatted_str = "".join(new_str)
        print(bracket_index)
        print(char_count)
                
        self.expand_helper(new_str, [], results, bracket_index)
        print(new_str)
        return results
