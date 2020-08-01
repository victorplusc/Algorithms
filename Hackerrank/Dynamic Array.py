#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

class Seq():
    def __init__(self, N):
        self.seqs = [[] for _ in range(N)]
        self.last_ans = 0
        self.N = N
        
    def query1(self, x, y):
        self.seqs[(x^self.last_ans)%self.N].append(y)
        
    def query2(self, x, y):
        seq = self.seqs[(x^self.last_ans)%self.N]
        self.last_ans = seq[y%len(seq)]
        return self.last_ans

def dynamicArray(n, queries):
    # Write your code here
    seq = Seq(n)
    
    q2s = []
    for v, x, y in queries:
        if v == 1:
            seq.query1(x, y)
        else:
            q2s.append(seq.query2(x, y))
    
    return q2s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
