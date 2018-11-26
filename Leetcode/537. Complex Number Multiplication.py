#537. Complex Number Multiplication
"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
"""

def complexNumberMultiply(x : "String 'a+bi'", y : "String: `a+bi`"):
    xComponents = x.split('+')
    xComponents[0] = int(xComponents[0])
    xComponents[1] = int(xComponents[1][0:len(xComponents[1])-1])
    yComponents = y.split('+')
    yComponents[0] = int(yComponents[0])
    yComponents[1] = int(yComponents[1][0:len(yComponents[1])-1])

    imaginaryReal = -1 * xComponents[1] * yComponents[1]
    imaginarySeg = xComponents[0] * yComponents[1] + yComponents[0] * xComponents[1]
    realSeg = xComponents[0] * yComponents[0] + imaginaryReal

    return "".join([str(realSeg),'+',str(imaginarySeg),'i'])

#Time complexity: O(1)
#Space complexity: O(1)
