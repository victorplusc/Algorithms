"""
914. X of a Kind in a Deck of Cards
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.

Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].

Constraints:
1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
"""
# Time complexity: O(N log N)
# Space complexity: O(N)
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def get_gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        count = list(collections.Counter(deck).values())
        gcd = count[0]
        for i in range(1, len(count)):
            gcd = get_gcd(gcd, count[i])
        
        return gcd > 1
