"""
The h-index is the largest number h such that there are h elements in the array that are of at least size h.
"""

##### Efficient algorithm







##### BRUTE FORCE

# Time complexity: O(N^2)
# Space complexity: O(N)

def find_h_index(publications: [int]) -> int:
    counts = {}
    for val in publications:
        counts[val] = counts.get(val, 0) + 1
    
    h_index = 0
    sorted_p = sorted((k,v) for (k,v) in counts.items())
    
    for i, (k, v) in enumerate(sorted_p):
        
        if h_index < k:
            if h_index <= v:
                h_index = k
            else:
                occurrences = 0
                for pair in sorted_p[i:]:
                    occurrences += pair[1]
                    if occurrences >= k:
                        h_index = k
                        break
    return h_index
