"""
299. Bulls and Cows
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_vals = collections.Counter()
        guess_vals = collections.Counter()
        bulls = 0
        
        for i, (c1, c2) in enumerate(zip(secret, guess)):
            if c1 == c2:
                bulls += 1
            else:
                secret_vals[c1] += 1
                guess_vals[c2] += 1
                
        cows = 0
        for val in guess_vals:
            cows += min(guess_vals[val], secret_vals[val])
              
        return "{0}A{1}B".format(bulls, cows)
