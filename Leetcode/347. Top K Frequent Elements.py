"""
Given a non-empty array of integers, return the k most frequent elements.
"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for num in nums:
            d[num] = d.get(num,0) + 1
        
        if len(d) == k:
            return [i for i in d]
        
        return heapq.nlargest(k, d.keys(), key = d.get)
