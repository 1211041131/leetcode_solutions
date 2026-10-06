# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if root==None:
            return 0
        queue=deque()
        queue.append([root,1])
        mini=0
        while queue:
            node,depth=queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append([node.left,depth+1])
            if node.right:
                
                queue.append([node.right,depth+1])

        
        


                

        