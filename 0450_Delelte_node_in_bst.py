class Solution(object):
    def deleteNode(self, root, key):

        if root == None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left == None and root.right == None:
                return None

            if root.left == None:
                temp1 = root.right
                return temp1


            if root.right == None:
                temp2 = root.left
                return temp2
            temp1 = root.right
            while temp1.left != None:
                temp1 = temp1.left
            temp2 = temp1

            root.val = temp2.val

            root.right = self.deleteNode(root.right, temp2.val)

        return root