"""
767. Reorganize String
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s: return s

        n = len(s)
        counter = collections.Counter(s)
        rev_map = collections.defaultdict(list)

        for val in counter:
            rev_map[counter[val]].append(val)

        most_common = []
        for i in reversed(range(n+1)):
            if i not in rev_map: 
                continue
            for c in rev_map[i]:
                most_common.append((c, i))

        if most_common[0][1] > (n+1)//2:
            return ""

        A = [""] * n

        idx = 0
        for key, count in most_common:
            for _ in range(count):
                A[idx] = key
                idx += 2
                if idx >= n:
                    idx = 1

        return "".join(A)
