"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        return two_pointers(height)

def dp_linear(height):
    if height == []:
        return 0
    water = 0
    size = len(height)
    
    left_max = [0 for _ in range(size)]
    left_max[0] = height[0]
    for i in range(1, size):
        left_max[i] = max(height[i], left_max[i-1])
        
    right_max = [0 for _ in range(size)]
    right_max[-1] = height[-1]
    for i in range(size-2, 0, -1):
        right_max[i] = max(height[i], right_max[i+1])
    
    for i in range(1, size - 1):
        col = min(left_max[i], right_max[i]) - height[i]
        water += col
    
    return water

def two_pointers(height):
    left = 0
    right = len(height) - 1
    water = 0
    left_max = right_max = 0
    
    while left < right:
        if (height[left] < height[right]):
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
            
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
        
    return water
        
# def stack_linear(height):
#     water = 0
#     current = 0
#     stack = []
    
#     while current < len(height):
#         while stack and height[current] > height[stack[-1]]:
#             top = stack.pop()
#             if not stack:
#                 break
#             distance = current - stack[-1] - 1
#             bounded_height = min(height[current], height[stack[-1]]) - height[top]
#             water += distance * bounded_height
#         current += 1
#         stack.append(current)
        
#     return water
