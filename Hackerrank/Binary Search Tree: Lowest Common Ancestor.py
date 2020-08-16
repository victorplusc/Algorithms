# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter your code here
    best = None
    def helper(node):
        nonlocal best
        if not node:
            return False
        
        mid = node.info == v1 or node.info == v2
        left = helper(node.left)
        right = helper(node.right)
        if mid+left+right >= 2:
            best = node
        return mid or left or right
    
    helper(root)
    return best
