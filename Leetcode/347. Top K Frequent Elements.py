"""
Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.heap_method(nums, k)
        return self.bucket_sort(nums, k)

    # Time complexity: O(N)
    # Space complexity: O(N)
    def bucket_sort(self, nums, k):
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        counter = collections.Counter(nums)
        for n in counter:
            bucket[counter[n]].append(n)

        k_most_freq = []
        for i in reversed(range(len(bucket))):
            for val in bucket[i]:
                if k == 0: 
                    break
                k_most_freq.append(val)
                k -= 1
        return k_most_freq

    # Time complexity: O(N log K)
    # Space complexity: O(N)
    def heap_method(self, nums, k):
        heap = []
        freq = collections.Counter(nums)

        for n in freq:
            if len(heap) < k:
                heapq.heappush(heap, [freq[n], n])
            else:
                heapq.heappushpop(heap, [freq[n], n])
        return [pair[1] for pair in heap]
