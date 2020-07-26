"""
Sentence Reverse
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
"""
def reverse_words(arr):
  def reverse_partial(i, j):
    while i < j:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1
  
  n = len(arr)
  reverse_partial(0, n-1)
  
  start = 0
  for end in range(n):
    if arr[end] == " ":
      reverse_partial(start, end-1)
      start = end+1
  
  reverse_partial(start, n-1)
  return arr
