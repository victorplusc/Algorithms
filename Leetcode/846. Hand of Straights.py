"""
846. Hand of Straights
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # return self.naive(hand, W)
        # return self.optimized_once(hand, W)
        return self.optimized_twice(hand, W)

    # Time complexity: O(N**2/W)
    # Space complexity: O(N)
    def naive(self, hand, W):
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] -= 1
        return True
    
    # Time complexity: O(N*log N + NW)
    # Space complexity: O(N)
    def optimized_once(self, hand, W):
        count = collections.Counter(hand)
        for i in sorted(count):
            if count[i] > 0:
                for j in range(W)[::-1]:
                    count[i+j] -= count[i]
                    if count[i+j] < 0:
                        return False
        return True
    
    # Time complexity: O(N*log N + N)
    # Space complexity: O(N)
    def optimized_twice(self, hand, W):
        count = collections.Counter(hand)
        start = collections.deque()
        last_checked = -1, 
        opened = 0
        for i in sorted(count):
            if opened > count[i] or (opened > 0 and i > last_checked + 1): return False
            start.append(count[i] - opened)
            last_checked = i
            opened = count[i]
            if len(start) == W:
                opened -= start.popleft()
        return opened == 0
    
