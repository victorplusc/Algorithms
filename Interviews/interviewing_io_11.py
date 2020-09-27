# You are given a string, you need to generate all the possible distinct subsets using characters of the givne string.
# "AAB" -> ["A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"]

import collections
def generate_subsets(s):
    n = len(s)
    total_counter = collections.Counter(s)
    def backtrack(current_perm=[], current_counter=collections.Counter()): #, current_counter={}
        if current_perm:
            output.add("".join(current_perm))
        if len(current_perm) == n:
            return
        
        for c in total_counter:
            if current_counter[c] == total_counter[c]: continue
            current_counter[c] += 1
            current_perm.append(c)
            backtrack(current_perm, current_counter)
            current_counter[c] -= 1
            current_perm.pop()

    output = set()
    backtrack()
    return list(output)
    
def count_subarray_max(A, left, right):
    n = len(A)
    total = 0
    
    for i in range(n):
        current_max = float('-inf')
        for j in range(i, n):
            # print(A[j])
            current_max = max(current_max, A[j])
            if current_max <= right:
                total += 1
            else:
                break

    return total
