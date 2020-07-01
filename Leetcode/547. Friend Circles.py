"""
547. Friend Circles
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        return self.bfs_method(M)
        return self.dfs_method(M)
    
    # Time complexity: O(N**2)
    # Space complexity: O(N)
    def bfs_method(self, M):
        n = len(M)
        q = collections.deque()
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                q.append(i)
                while q:
                    k = q.popleft()
                    visited.add(k)
                    for j in range(n):
                        if M[k][j] == 1 and j not in visited:
                            q.append(j)
                count += 1
        return count
    
    # Time complexity: O(N**2)
    # Space complexity: O(N)
    def dfs_method(M):
        n = len(M)
        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
