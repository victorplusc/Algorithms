"""
1051. Height Checker
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)
"""

# Time complexity: O(N log N)
# Space complexity: O(N)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        in_order = sorted(heights)
        to_move = 0
        for i in range(len(in_order)):
            if in_order[i] != heights[i]:
                to_move += 1
        return to_move
