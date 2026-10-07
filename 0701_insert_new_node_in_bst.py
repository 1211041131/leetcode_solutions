# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        new_node=TreeNode(val)
        if root==None:
            root=new_node
            return root
        if root.val>val:
          
            root.left=self.insertIntoBST(root.left,val)
        else:
         
            root.right=self.insertIntoBST(root.right,val)

        return root  