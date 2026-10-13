# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        first=[None]
        second=[None]
        prev=[None]
        middle=[None]
        def inorder(node):

            if node==None:
                return 
            inorder(node.left)
            if prev[0]!=None and prev[0].val>node.val:
                if first[0] is None:
                    first[0]=prev[0]
                    middle[0]=node
                else:
                    second[0]=node
            prev[0]=node
            inorder(node.right)
        inorder(root)
        if second[0]:
            first[0].val,second[0].val=second[0].val,first[0].val
        else:
            first[0].val,middle[0].val=middle[0].val,first[0].val

