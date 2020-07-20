"""
863. All Nodes Distance K in Binary Tree
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        def make_graph(parent, root):
            if not root: return
            graph[parent].append(root)
            graph[root].append(parent)
            make_graph(root, root.left)
            make_graph(root, root.right)
        make_graph(None, root)
        
        q = collections.deque([(target, 0)])
        visited = set()
        while q:

            if q[0][1] == K:
                return [node.val for node, d in q]
            
            node, d = q.popleft()
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited and nei:
                    q.append([nei, d+1])
        return []
