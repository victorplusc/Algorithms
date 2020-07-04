"""
1198. Find Smallest Common Element in All Rows
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

Example 1:
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5 

Constraints:
1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # return self.hashmap(mat)
        # return self.bin_search(mat)
        return self.row_positions(mat)
    
    # Time complexity: O(R*C)
    # Space complexity: O(R)
    def row_positions(self, mat):
        n, m = len(mat), len(mat[0])
        pos = [0] * n
        curr_max = count = 0
        while True:
            for i in range(n):
                while pos[i] < m and mat[i][pos[i]] < curr_max:
                    pos[i] += 1
                if pos[i] >= m:
                    return -1
                if mat[i][pos[i]] != curr_max:
                    count = 1
                    curr_max = mat[i][pos[i]]
                else:
                    count += 1
                    if count == n:
                        return curr_max
                
    # Time complexity: O(R*C log C)
    # Space complexity: O(1)
    def bin_search(self, mat):
        def search(arr, target):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        n, m = len(mat), len(mat[0])
        for i in range(m):
            found = True
            for j in range(1, n):
                found &= search(mat[j], mat[0][i])
            if found: return mat[0][i]
        return -1
        
    # Time complexity: O(R*C)
    # Space complexity: O(R*C)
    def hashmap(self, mat):
        count = collections.Counter()
        for row in mat:
            for val in row:
                count[val] += 1
                if count[val] == len(mat):
                    return val
        return -1
