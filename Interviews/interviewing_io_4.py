# Let Operation be some struct with fields http_method and data:
# struct Operation {
#   http_method: HTTPMethod,
#   Data: String
# }

# and HTTPMethod some enumeration of valid HTTP verbs:
# enum HTTPMethod {
#   Get,
#   Post,
#   Put,
#   Delete,
# }

# Write a function called process_in_order() that takes a vector of operations and returns a vector of results. The order of results should correspond to the order of the input operations (i.e. the first result element should be the response to the first operation), but the operations should be processed in a different order, specifically in order of the method as follows:

# 1)DELETE
# 2)POST
# 3)PUT
# 4)GET

# Assume you can call process_operation() on a single operation to get back a single result. You should not have to implement a sorting algorithm.

# For example, if I receive
# [{ GET, "a" }, { POST, "ab" }, { POST, "abb"} ,{ PUT, "abc" }]
# I want to process it in the order
# [{POST, "abb"}{ POST, "ab" }, { PUT, "abc" }, { GET, "a" }]

# Let’s say procees_operation() just gives you the length of the input string, then we’ll get 
# process_operation({POST, "ab"}) => 2
# process_operation({PUT, "abc"}) => 3
# process_operation({GET, "a"}) => 1

# So we want process_in_order() to return
# [3, 1, 2]

"""
In the case of one big list:

[ ["DELETE", ... ], ["POST", ... ] ]

for array in arrays:
    unpack(array)

for unpacking:
    1) input: [1,2,3,4]
    2) output: 1, 2, 3, 4

"""

# Time complexity: O(N)
# Space complexity: O(N)

def process_in_order(operations: [tuple]) -> [int]:
    delete_list = []
    post_list = []
    put_list = []
    get_list = []
    positions = {}
    processed_operations = [None for i in range(len(operations))]
    
    for i, op in enumerate(operations):
        positions[op] = i
        
        if "DELETE" in op:
            delete_list.append(op)
        elif "POST" in op:
            post_list.append(op)
        elif "PUT" in op:
            put_list.append(op)
        else:
            get_list.append(op)
    
    for op_list in [delete_list, post_list, put_list, get_list]:
        for op in (op_list):
            processed_operations[positions[op]] = process_operation(op)
    
    return processed_operations
            
# For example, if I receive
# [{ GET, "a" }, { POST, "ab" }, { POST, "abb"} ,{ PUT, "abc" }]
# I want to process it in the order
# [{POST, "abb"}{ POST, "ab" }, { PUT, "abc" }, { GET, "a" }] 
            
def process_operation(operation):
    return len(operation[1])
           
print(process_in_order([("GET", "a"), ("POST", "ab"), ("DELETE", "abba"), ("POST", "abb"), ("PUT", "abc")]))
