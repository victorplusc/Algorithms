# Only need to `import functools` for `reduce`, as it typically does not help readability.

"""
Lambda function syntax:

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
Map function:

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

# prints ['32', '053'], is an iterator, so when it is incremented, previous indices are not saved
print(list(mapped))

"""
Filter function:

a) Takes as input:
    1) expression
    2) iterable
    
b) returns an iterator object where the expression is True
"""

array = [1,2,5,4,3,7,39,3,6,8,9,4,9,4,87,53,1]
filtered = filter(lambda x : x > 10, array)

# returns [39, 87, 53]
print(list(filtered))

array = [0, 0, 1, 1, 0, 1]
filtered = filter(None, array)

# returns [1, 1, 1]
print(list(filtered))
