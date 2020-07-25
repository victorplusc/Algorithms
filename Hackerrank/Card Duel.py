"""
Card duel is a really simple card game played between two players. In this game, player 1 is given k1 cards and player 2 is given k2 cards. Each card is given a value from 1 to N where N is the number of cards. The objective of the game is to acquire all the cards.

During each turn, each player chooses one card from their hand for the duel. The player with the higher value card wins the turn and will add both the cards used during the duel into their hands.

Example:
Given 5 cards valued {1, 2, 3, 4, 5}. Player 1 is given the cards 5, 4 and 1 and Player 2 is given the cards 2 and 3.

In the first round, Player 1 plays the card 4 and Player 2 plays the card 3. Since 4 > 3, Player 1 wins the round. Player 1 adds the card 4 back into his hand and takes the card 3.

In the second round, Player 1 plays the card 3 and Player 2 plays the card 2. Since 3 > 2, Player 1 wins the round. Player 1 add the card 3 back into his hand and takes the card 2.

Player 2 no longer has any cards so Player 1 wins.

Given T test cases your goal is to output "YES" or "NO" whether player 1 can win the game assuming both players play optimally.

The first line gives you T test cases.

The first line in each test case gives you the value N, k1, and k2.

The next line contains k1 integers denoting player 1's hand.

The last line of the test case contains k2 integers denoting player 2's hand.
"""
import sys

def play(N, k1, k2, p1, p2):
    if N in p1:
        print("YES")
    else:
        print("NO")
    
import collections
i = 0
T = 0
p1 = []
p2 = []
q = collections.deque()
for line in sys.stdin:
    q.append(line.strip("\n").split(" "))

tests = int(q.popleft()[0])
for i in range(tests):
    N = q[0][0]
    k1 = q[0][1]
    k2 = q[0][2]
    p1 = q[1]
    p2 = q[2]

    play(N, k1, k2, p1, p2)
    
    for _ in range(3):
        q.popleft()

