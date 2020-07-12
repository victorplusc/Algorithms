"""
93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
# Time complexity: O(3**N)
# Space complexity: O(3**N)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, segments, curr):
            if len(s) > segments*3:
                return
            if segments == 0:
                output.append(".".join(curr))
            else:
                for i in range(min(3, len(s)-segments+1)):
                    if (i == 2 and int(s[:3]) > 255) or (i > 0 and s[0] == "0"):
                        continue
                    curr.append(s[:i+1])
                    backtrack(s[i+1:], segments-1, curr)
                    curr.pop()
                    
        output = []
        backtrack(s, 4, [])
        return output
