"""
1079. Letter Tile Possibilities
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: "AAABBC"
Output: 188

Note:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(counter):
            seqs = 0
            for i in (chr(ord("A")+i) for i in range(26)):
                if counter[i] == 0: continue
                seqs += 1
                counter[i] -= 1
                seqs += dfs(counter)
                counter[i] += 1
            return seqs
        
        counter = collections.Counter(tiles)
        return dfs(counter)
