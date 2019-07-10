"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))
