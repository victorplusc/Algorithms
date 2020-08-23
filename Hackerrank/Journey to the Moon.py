#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
import collections
def journeyToMoon(n, astronaut):
    components = collections.defaultdict(set)
    parent = dict()
    def union(x, y):
        x = find(x)
        y = find(y)
        components[x] = components[x].union(components[y])
        for element in components[y]:
            parent[element] = x
        if y in components:
            del components[y]
    
    def find(x):
        return parent[x]

    for i in range(n):
        components[i].add(i)
        parent[i] = i
    
    for edge in astronaut:
        if find(edge[0]) != find(edge[1]):
            union(edge[0], edge[1])
    
    ans = int(n*(n-1)/2)
    for k, v in components.items():
        x = len(v)
        if x > 1:
            ans -= int(x*(x-1)/2)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
