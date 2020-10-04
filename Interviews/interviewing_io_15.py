"""
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

# Example 4:
# Input: s = "1"
# Output: 1
"""
"""
1) We have 2 possible outputs if 10 <= "__" <= 26
2) otherwise, we have 1 output (1 <= "_" <= 9)
3) algorithm could look something like this:


n = len(s)
if n == 0 or s[0] == "0":
    return 0

dp = [0] * n

dp[0] = 1
for i in range(n-1):
    if s[i+1] == "0" and s[i] not in ["1", "2"]:
        return 0
    elif 10 <= int(s[i]+s[i+1]) <= 26:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = dp[i]
        
return dp[-1]

"s = "12345"
         ^^
      
output = 3

i = 1
dp = [1, 2, 3, 3, 3]
"""

def decode_string(s):
    n = len(s)
    if n == 0 or s[0] == "0":
        return 0

    ways = 1
    for i in range(n-1):
        if s[i+1] == "0" and s[i] not in ["1", "2"]:
            return 0
        elif 10 <= int(s[i]+s[i+1]) <= 26:
            ways += 1

    return ways

# print(decode_string("12"))
# print(decode_string("226"))
# print(decode_string("0"))
# print(decode_string("12345"))
  
'''
Given length of a circular array length “n” and an array of paths from the starting node to the ending node. Determine the node that is most visited after traversing through all the nodes. If there are multiple nodes with highest number of visits, return the node with least index.

•    Circular array is a array where the last node is connected to the first node.

Example 1:

n = 3 (our circular array will be [1,2,3])
arr = [1,3,2,3]

1 -> 3 (1  2  3)
3 -> 2 (3  1  2) The last node in the array is 3 which is connected to the first node 1
2 -> 3 (2  3)

2 & 3 are the most visited nodes in the example above. Our function will return “2” as node 2 has the lowest index. 
Example 2:

n = 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, ... 1, 2, 3, 4, 5]
arr = [1,5,10,5]

1 -> 5 (1  2  3  4  5)
5 -> 10 (5  6 78910)
10 -> 5 (10  12345)

Ans: 5
'''

"""
1) create the graph, connect the last node to the first, when i == n, graph[i] = 1
2) iterate over the graph, using our queries, and mark nodes, potentially using an array [0] * n, A[i-1] += 1

graph = collections.defaultdict() # {}

for i in range(1, n):
    graph[i] = i+1
graph[n] = 1

marked_nodes = [0] * n
curr = 1
for node in (arr):
    marked_nodes[node-1] += 1
    while curr != node:
        marked_nodes[curr-1] += 1
        curr = graph[curr]
return max(marked_nodes)

3) return max(marked_nodes)


n = 3 (our circular array will be [1,2,3])
arr = [1,3,2,3]

1 -> 3 (1  2  3)
3 -> 2 (3  1  2) The last node in the array is 3 which is connected to the first node 1
2 -> 3 (2  3)

graph = {
    1 : 2,
    2: 3,
    3: 1
}
marked_nodes = [1, 1, 0]
curr = 3
"""
import collections
def traverse_circular_array(n, arr):
    
    graph = collections.defaultdict() # {}

    for i in range(1, n):
        graph[i] = i+1
    graph[n] = 1

    marked_nodes = [0] * n
    marked_nodes[0] = -1
    curr = 1
    for node in (arr):
        marked_nodes[node-1] += 1
        while curr != node:
            marked_nodes[curr-1] += 1
            curr = graph[curr]

    best = (0, None)
    for i, val in enumerate(marked_nodes):
        if val > best[0]:
            best = (val, i+1)
    return best[1]

print(traverse_circular_array(3, [1,3,2,3]))
print(traverse_circular_array(10, [1,5,10,5]))
