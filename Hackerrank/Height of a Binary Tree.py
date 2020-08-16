# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left) + 1
        right = dfs(node.right) + 1
        return max(left, right)
    return dfs(root)-1
