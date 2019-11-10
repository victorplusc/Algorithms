"""
1055. Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:
  - Both the source and target strings consist of only lowercase English letters from "a"-"z".
  - The lengths of source and target string are between 1 and 1000.
"""
class Solution:
    # Time complexity: O(N*M)
    # Space complexity: O(1)
    def shortestWay(self, src: str, tar: str) -> int:
        count = 0
        i = 0
        while i < len(tar):
            curr_i = i
            for j in range(len(src)):
                if i < len(tar) and src[j] == tar[i]:
                    i += 1
            if i == curr_i:
                return -1
            count += 1
        return count
    
    # Time complexity: O(log(N)*M), where N is len(s)
    # Space complexity: O(N)
    import collections
    def shortestWay(self, s: str, t: str) -> int:
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        
        idx = 0
        count = 1
        for c in t:
            if c not in d:
                return -1
            else:
                temp = d[c]
                if temp[-1] < idx:
                    count += 1
                    idx = 0
                idx = self.binarysearch(temp, idx)
                
        return count
                    
    def binarysearch(self, A, idx):
        lo = 0
        hi = len(A)-1
        while lo < hi:
            mid = (lo+hi)//2
            if A[mid] < idx:
                lo = mid+1
            else:
                hi = mid
    
        return A[lo]+1
