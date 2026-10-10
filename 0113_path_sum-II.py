class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def solve(root, path, total):
            if root == None:
                return

            path.append(root.val)
            total += root.val

            if root.left == None and root.right == None:
                if total == targetSum:
                    result.append(path[:])
            else:
                solve(root.left, path[:], total)
                solve(root.right, path[:], total)

        solve(root, [], 0)
        return result