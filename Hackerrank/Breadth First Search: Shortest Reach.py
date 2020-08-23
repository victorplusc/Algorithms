#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
import collections
def bfs(n, m, edges, s):
    graph = collections.defaultdict(list)
    for p, q in edges:
        graph[p].append(q)
        graph[q].append(p)

    dists = collections.defaultdict()
    q = collections.deque([[s, 0]])
    visited = set()
    while q:
        front, depth = q.popleft()
        

        for nei in graph[front]:
            if nei in visited: 
                continue
            dists[nei] = depth+6
            visited.add(nei)
            q.append([nei, depth+6])
    
    return [dists[i] if i in dists else -1 for i in range(1, n+1) if i != s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
