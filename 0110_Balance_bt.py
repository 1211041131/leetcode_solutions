```python
class Solution(object):
    def isBalanced(self, root):

        def height(root):
            if root == None:
                return 0

            left = height(root.left)
            right = height(root.right)

            return max(left, right) + 1

        if root == None:
            return True

        if abs(height(root.left) - height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
```