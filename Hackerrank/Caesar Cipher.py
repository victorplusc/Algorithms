#!/bin/python3

import math
import os
import random
import re
import sys

"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""

# Complete the caesarCipher function below.
# middle-Outz 2 -> okffng-Qwvb
def caesarCipher(s, k):
    up_order = {i:chr(ord('A')+i) for i in range(26)}
    lo_order = {i:chr(ord('a')+i) for i in range(26)}
    rev_up_order = {chr(ord('A')+i):i for i in range(26)}
    rev_lo_order = {chr(ord('a')+i):i for i in range(26)}

    encrypted = []
    
    for c in s:
        if c.isalpha():
            if c in rev_lo_order:
                new = lo_order[(rev_lo_order[c]+k)%26]
                encrypted.append(new)
            elif c in rev_up_order:
                new = up_order[(rev_up_order[c]+k)%26]
                encrypted.append(new)
        else:
            encrypted.append(c)
    return "".join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
