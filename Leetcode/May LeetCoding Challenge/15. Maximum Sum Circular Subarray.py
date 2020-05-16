class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total, highest, curr_max, lowest, curr_min = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curr_max = max(curr_max + a, a)
            highest = max(highest, curr_max)
            curr_min = min(curr_min + a, a)
            lowest = min(lowest, curr_min)
            total += a
        return max(highest, total - lowest) if highest > 0 else highest
