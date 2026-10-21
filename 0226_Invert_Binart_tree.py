# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def invertTree(self, root):
        if root==None:
            return None 
        queue=deque()
        queue.append(root)
        while len(queue):
            i=queue.popleft()
            i.left,i.right=i.right,i.left
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        return root 
