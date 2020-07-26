"""
1345. Jump Game IV
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

Example 2:
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.

Example 3:
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Example 4:
Input: arr = [6,1,9]
Output: 2

Example 5:
Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3

Constraints:
1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        locations = collections.defaultdict(list)
        for i, n in enumerate(arr):
            locations[n].append(i)
        
        q = collections.deque([0])
        target = len(arr)-1
        visited = {0}
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                visited.add(i)
                
                if i == target:
                    return steps

                if i+1 not in visited and i+1 < target+1:
                    q.append(i+1)
                    visited.add(i+1)

                if i-1 not in visited and i-1 >= 0:
                    q.append(i-1)
                    visited.add(i-1)

                for j in locations[arr[i]]:
                    q.append(j)
                    visited.add(j)
                del locations[arr[i]]
                
            steps += 1
        return -1
