# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root== None:
            return False 
        current_sum=root.val

        if root.left == None and root.right == None:
            if current_sum == targetSum:
                return True
            return False

        l=self.hasPathSum(root.left, targetSum-current_sum)
        r=self.hasPathSum(root.right, targetSum-current_sum)
        
        return l or r

 