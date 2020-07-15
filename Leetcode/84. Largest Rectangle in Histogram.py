"""
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        width = len(heights)
        
        largest = 0
        left = [-1]
        heights.append(0)
        for right in range(width+1):
            while heights[right] < heights[left[-1]]:
                h = heights[left.pop()]
                w = right-1-left[-1]
                largest = max(largest, h*w)
            left.append(right)
        return largest
