# Only need to `import functools` for `reduce`, as it typically does not help readability.

"""
=========================================================================================
Lambda function syntax:
=========================================================================================

f = lambda arg_0, arg_1, ... : output

e.g.

f = lambda x, y: print(x + y)
"""

d = {
        "Apples" : 5,
        "Oranges": 6,
        "Bananas": 3,
        "Peaches": 9
    }

def print_sorted_dict(d: dict) -> None:
    for k, v in sorted(d.items(), key=lambda pair : pair[1]):
        print(k, v)
print_sorted_dict(d)
    
import functools
prod = lambda A: functools.reduce(operator.mul, A)
print(prod([1,2,3,4,5,6,7]))

"""
=========================================================================================
Map function:
=========================================================================================

a) Takes as input:
    1) function
    2) iterable
    
b) returns an iterator object with the input function mapped to the output

e.g. 
I: x = map(f, [1,2,3])
O: f(1), f(2), f(3)
"""

mapped = map(lambda val: str(val[1]) + str(val[0]), [(1,2), (2,3), (53,0)])

print(next(mapped))
print(list(mapped)) # prints ['32', '053'], is an iterator, so when it is incremented, previous indices are not saved

"""
=========================================================================================
Filter function:
=========================================================================================

a) Takes as input:
    1) function
    2) iterable
    
b) returns an iterator object where the function is True
"""

array = [1,2,5,4,3,7,39,3,6,8,9,4,9,4,87,53,1]
filtered = filter(lambda x : x > 10, array)
print(list(filtered)) # returns [39, 87, 53]

array = [0, 0, 1, 1, 0, 1]
filtered = filter(None, array)
print(list(filtered)) # returns [1, 1, 1]

"""
=========================================================================================
Reduce function:
=========================================================================================

a) Takes as input:
    1) function
    2) iterable

b)
    1) val_1 = f(A[0], A[1])
    2) val_2 = f(val_1, A[2])
    3) val_3 = f(val_2, A[3])
    ...
    n-1) val_n = f(val_n-1, A[-1])

"""

array = [x*x for x in range(5)]
sum_odd = lambda x, y: x+y if y%2 != 0 else x*1
y = functools.reduce(sum_odd, array)

print(array) # [0, 1, 4, 9, 16]
print(y)     # 10


"""
=========================================================================================
Zip function:
=========================================================================================

a) Takes as input:
    1) iterable
    2) iterable
    ...
    n) iterable
    
b) returns an iterable with all elements in the same order joined together, up until the smallest iterable is depleted.

e.g.

zip([1,2,3,4], ("a", "b", "c"), [50, 100, 150, 200, 250])
>>> iterable((1,"a",50), (2, "b", 100), (3, "c", 150))

Note:
- if no parameters are passed, zip() returns an empty iterator.
- if a single iterable is passed, returns an iterator of 1-tuples
"""

zipped = zip([1,2,3,4], ("a", "b", "c"), [50, 100, 150, 200, 250])
print(list(zipped)) #[(1, 'a', 50), (2, 'b', 100), (3, 'c', 150)]
print(list(zip())) #[]
print(list(zip([1,2,3]))) #[(1,), (2,), (3,)]
print(len((1,))) #prints 1
