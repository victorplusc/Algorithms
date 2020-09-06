"""
835. Image Overlap
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes: 
1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""
# Time complexity: O(N**4)
# Time complexity: O(1)
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        dim = len(A)
        
        def shift_and_count(x_shift, y_shift, M, R):
            count = 0
            for ry, my in enumerate(range(y_shift, dim)):
                for rx, mx in enumerate(range(x_shift, dim)):
                    if M[my][mx] == 1 and M[my][mx] == R[ry][rx]:
                        count += 1
            return count
        
        max_overlaps = 0
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))
        return max_overlaps
