# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = [0]

        def maxi(node):
            if node == None:
                return 0

            left = maxi(node.left)
            right = maxi(node.right)

            diameter[0] = max(diameter[0], left + right)

            return 1 + max(left, right)

        maxi(root)
        return diameter[0]