#709. To Lower Case
"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""

def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    newStr = []
    lowerBound = ord('A')
    upperBound = ord('Z')

    for i in range(len(str)):
        charVal = ord(str[i])
        if lowerBound <= charVal <= upperBound:
            newStr.append(chr(charVal+32))
        else:
            newStr.append(str[i])

    return "".join(newStr)

#Time complexity: O(N)
#Space complexity: O(N)
