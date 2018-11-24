#1.3 URLify
"""
URLify: Write a method to replace all spaces in a string with '%20'.
"""

def URLify(s: "String"):
    sList = list(s.strip())
    for i in range(len(sList)):
        if sList[i] == " ":
            sList[i] = "%20"
    return "".join(sList)

#Time Complexity: O(N)
#Space Complexity: O(N)
