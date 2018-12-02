#461. Hamming Distance

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.
"""

def hammingDistance(x, y):

    x = x ^ y
    distance = 0

    while x:
        x = x & (x - 1)
        distance += 1

    return distance
