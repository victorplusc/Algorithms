# input = 2 3 2 4 5
# result = 120 80 120 60 48

"""
left_prod = []
right_prod = []

[2, 3, 2, 4, 5]
    ^

left_prod = [2]
right_prod = [3 * 2 * 4 * 5, 2 * 4 * 5]

A[1:]
[2, 0, 1] = 0

[0, 0/0,0]

product = (i, 2 * 3 * 2 * 5)
for all elements:
    res[i] = product/A[i]
    
product = prod(A)
zero_counter = 0

results = [0 for _ in range(len(A))]

for i, val in enumerate(A):

    if val == 0:
        zero_counter += 1
        if zero_counter > 1:
            return [0 for _ in range(len(A))]
        
        results[i] = prod(A[:i-1]) * prod(A[i+1:])
        return results
    
    results[i] = product/val

return results
    
"""

def prod_except_index(A: [int]) -> [int]:
    product = prod(A)
    results = [0 for _ in range(len(A))]

    for i, val in enumerate(A):
        if val == 0:
            results[i] = prod(A[:i]) * prod(A[i+1:])
            return [int(i) for i in results]
        results[i] = product/val
        
    return [int(i) for i in results]


def prod(A: [int]) -> int:
    p = 1
    for val in A:
        p*=val
    return p
