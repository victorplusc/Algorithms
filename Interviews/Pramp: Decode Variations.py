"""
Decode Variations
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:
input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
Constraints:

[time limit] 5000ms

[input] string S

1 ≤ S.length ≤ 12
[output] integer
"""
# Time complexity: O(N)
# Space complexity: O(1)
def decodeVariations(s):
  n = len(s)
  
  first = 1 if s[0] != 0 else 0
  second = 1
  for i in range(2, n+1):
    single = int(s[i-1])
    double = int(s[i-2:i])
    ways = 0
    if 1 <= single <= 9:
      ways += first
    if 10 <= double <= 26:
      ways += second
    second, first = first, ways
  return first
  
