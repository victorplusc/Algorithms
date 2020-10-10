# you are given a stack on n boxes, each with w, h, d. you are not allowed to rotate them,
# what maximum height you can get by stacking one on top of the other
# constraint: all the three dimension should be strictly decreasing

"""
input: A = [[w0, h0, d0], [w1, h1, d1] ... , [wn, hn, dn]]

Example
input: A = [[8, 5, 3], [5, 5, 5], [4, 4, 4]]
output: = 9

[5, 8, 3], [5, 5, 5], [4, 4, 4]
H: |            |
W: |       |
D: |   |

H: |       |
W: |       |
D: |       |

def f(A):
    best = 0
    
    n = len(A)
    def backtrack(start, curr_w, curr_h, curr_d, total):
        if start == n:
            best = max(best, total)
            return
        for i in range(start, n):
            w, h, d = A[i]
            if w < curr_w and h < curr_h and d < curr_d:
                backtrack(i+1, w, h, d, total+h)    
            backtrack(i+1, curr_w, curr_h, curr_d, total)
    
    for i, box in enumerate(A):
        curr_w, curr_h, curr_d = box
        backtrack(i, curr_w, curr_h, curr_d, curr_h)
    
    return best


for i, box in enumerate(boxes):
    initialize current limits, curr_w, curr_h, curr_d = box
    for j in range(i+1, n):
        w, h, d = A[j]
        if w < curr_w and h < curr_h and d < curr_d:
            curr_w, curr_h, curr_d = w, h, d
            
[8, 8, 8], [1, 7, 1], [7, 6, 7], [5, 5, 5], [4, 4, 4]

"""

# you are given a stream of integers, find at any given the function is called, it ll output the max product of k elements
"""
[-2, 0, 4], 2 => 4

import heapq
def function(A, k):
    contains_negative = False
    contains_zero = False
    pos_heap = []
    neg_heap = []

    for val in A:
        if len(pos_heap) < k and val > 0:
            heapq.heappush(pos_heap, val)
        elif val > 0:
            heapq.heappushpop(pos_heap, val)
        elif val < 0:
            contains_negative = True
            if len(neg_heap) < k and val < 0:
                heapq.heappush(neg_heap, -val)
            else:
                heapq.heappushpop(neg_heap, -val)
        else:
            contains_zero = True
    
    if not contains_negative:
        return prod(pos_heap)
    elif not pos_heap and len(neg_heap) == 1 and contains_zero:
        return 0
    
    max_prod = 1
    while k > 0:
        if k == 1:
            if pos_heap:
                max_prod *= pos_heap[0]
            break
        if len(neg_heap) >= 2:
            if len(pos_heap) >= 2:
                pos1 = pos_heap.pop()
                pos2 = pos_heap.pop()
                if pos1*pos2 < neg1*neg2:
                    max_prod *= neg1*neg2
                    k -= 2
                    heapq.heappush(pos_heap, pos1)
                    heapq.heappush(pos_heap, pos2)
                else:
                    max_prod *= pos1*pos2
                    k -= 2
                    heapq.heappush(neg_heap, neg1)
                    heapq.heappush(neg_heap, neg2)
            elif len(pos_heap) >= 1:
                pos = pos_heap.pop()
                if pos < neg1*neg2:
                    max_prod *= neg1*neg2
                    k -= 2
                    heapq.heappush(pos_heap, pos)
                else:
                    max_prod *= pos
                    k -= 1
                    heapq.heappush(neg_heap, neg1)
                    heapq.heappush(neg_heap, neg2)
            else:
                max_prod *= neg1*neg2
                k -= 2
        
    return max_prod

Time: O( N log K + K log K )
Space: O(K)
    
"""
