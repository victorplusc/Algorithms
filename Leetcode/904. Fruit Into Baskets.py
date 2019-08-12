"""
904. Fruit Into Baskets
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
"""

# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def totalFruit(self, tree):
        if len(tree) <= 2:
            return len(tree)
        
        max_basket = 0
        first_type = None
        second_type = None

        consec_fruits = 0
        current_basket = 0
        
        for fruit in tree:
            if first_type == None:
                first_type = fruit
            elif second_type == None and fruit != first_type:
                second_type = fruit
            
            if fruit in {first_type, second_type}:
                current_basket += 1
            else:
                current_basket = consec_fruits + 1
            
            if fruit == second_type:
                consec_fruits += 1
            else:
                consec_fruits = 1
            
            if fruit != second_type:
                first_type, second_type = second_type, fruit

            max_basket = max(max_basket, current_basket)
                
        return max_basket
