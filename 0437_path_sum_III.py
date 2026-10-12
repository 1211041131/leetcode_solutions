# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        def solve(root, total):
            if root == None:
                return 0 
            total=total+root.val
            count=0
            if total==targetSum:
                count+=1
            l=solve(root.left,total)
            r=solve(root.right,total)
            return r+l+count
        if root == None:
            return 0
        return (solve(root,0)+ self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))
