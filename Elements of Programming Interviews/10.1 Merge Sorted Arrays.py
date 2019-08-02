"""
10.1 Merge Sorted Arrays

Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence. For example, if the input is:

[
    [3, 5, 7],
    [0, 6],
    [0, 6, 28]
]

then the output should be:

[0, 0, 3, 5, 6, 6, 7, 8]
"""
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]] = []
    
    sorted_array_iters = [iter(x) for x in sorted_arrays]
    
    for i, index in enumerate(sorted_array_iters):
        first_element = next(index, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    result = []
    
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_array_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
            
    return result
