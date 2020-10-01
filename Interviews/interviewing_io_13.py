'''
List of integers is given. Return an array of all the elements' squares in ascending order.

[1, 2, 3, 4] -> [1, 4, 9, 16]
'''

def sorted_squared(A):
    output = []
    left = 0
    right = len(A)-1
    
    while left <= right:
        left_sq = A[left]*A[left]
        right_sq = A[right]*A[right]
        if left_sq > right_sq:
            output.append(left_sq)
            left += 1
        else:
            output.append(right_sq)
            right -= 1
    
    output.reverse()
    
    return output
    
'''
A = [[1,3], [5,6], [7,9]]
B = [[2,3], [5,7]]
output = [[2,3], [5,6], [7,7]]


A = |-------|      |---|   |--------|
B =     |---|      |-------|
O =     |   |      |   |   |         

A = [[1,3], [5,6], [7,9]]
                     i   
B = [[2,3], [5,7]]
              j
output = [[2, 3], [5, 6], [7, 7]]
'''
def merge_intervals(A, B):
    output = []
    i = j = 0
    while i < len(A[i]) and j < len(B[j]):
        A_start, A_end = A[i]
        B_start, B_end = B[j]

        if B_end < A_start:
            j += 1
            continue
        elif A_end < B_start:
            i += 1
            continue

        if B_start > A_start:
            if B_end <= A_end:
                output.append([B_start, B_end])
                j += 1
            else: # A_end < B_end
                output.append([B_start, A_end])
                i += 1
        else: #B_start <= A_start
            if B_end <= A_end:
                output.append([A_start, B_end])
                j += 1
            else: # A_end < B_end
                output.append([A_start, A_end])
                i += 1
    return output
