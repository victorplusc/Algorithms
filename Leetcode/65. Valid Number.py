"""
65. Valid Number
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def isNumber(self, s: str) -> bool:
        # return self.dfa(s)
        return self.conditionals(s)
        
    def dfa(self, s):
        states = [
            {},
            {"blank": 1, "sign": 2, "digit": 3, ".":4},
            {"digit": 3, ".": 4},
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            {"digit": 5},
            {"digit": 5, "e": 6, "blank": 9},
            {"sign": 7, "digit": 8},
            {"digit": 8},
            {"digit": 8, "blank": 9},
            {"blank": 9}
        ]
        curr_state = 1
        for c in s:
            if "0" <= c <= "9":
                c = "digit"
            if c == " ":
                c = "blank"
            if c in ["+", "-"]:
                c = "sign"
            if c not in states[curr_state].keys():
                return False
            curr_state = states[curr_state][c]
        if curr_state not in [3, 5, 8, 9]:
            return False
        return True

    def conditionals(self, s):
        s = s.strip()
        dec_seen = e_seen = num_seen = False 
        for i, c in enumerate(s):
            if "0" <= c <= "9":
                num_seen = True
            elif c == ".":
                if e_seen or dec_seen: return False
                dec_seen = True
            elif c == "e":
                if e_seen or not num_seen: return False
                e_seen = True
                num_seen = False
            elif c in ["+", "-"]:
                if i != 0 and s[i-1] != "e": return False
            else:
                return False
        return num_seen
