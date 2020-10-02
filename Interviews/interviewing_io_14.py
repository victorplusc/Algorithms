# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

"""
A = [1,2,3,1]
         ^
best = 4
curr = 4 -> prev+1 = 3
prev = 2 -> 4

iterate from i: 1 -> n:
    prev, curr = curr, prev + A[i]
    
    best = max(curr, prev)
return best

A = [1, 999, 50, 50, 50, 50]
"""

def rob_houses(A):
    n = len(A)

    curr = 0
    prev = 0
    
    for i in range(n):
        prev, curr = curr, prev + A[i]
    
    return max(prev, curr)
    
"""
Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Output: [1]
"""
# Time complexity: O(N + N log K + K) => O(N log K)
# Space complexity: O(N)

import collections
import heapq
def k_most_freq(nums, k):    
    counter = collections.Counter(nums)
    heap = []

    for val, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, val))
        else:
            heapq.heappushpop(heap, (freq, val))
    return [val for freq, val in heap]
