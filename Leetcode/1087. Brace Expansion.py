"""
1087. Brace Expansion
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.
"""

class Solution:
    def expand(self, s: str) -> List[str]:
        results = []
        dfs(s, 0, [], results)
        return results
    
def dfs(s: str, index: int, curr: [], results: List[int]):
    if index == len(s):
        results.append("".join(curr))
        return

    c = s[index]

    if c == "{":
        char_list = []
        end_index = index + 1
        while end_index < len(s) and s[end_index] != "}":
            if s[end_index] != ",":
                char_list.append(s[end_index])
            end_index += 1

        char_list.sort()
        for x in char_list:
            curr.append(x)
            dfs(s, end_index + 1, [_ for _ in curr], results)
        
    elif c not in {",", "}"}:
        curr.append(c)
        dfs(s, index + 1, [_ for _ in curr], results)
