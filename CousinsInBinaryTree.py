# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # Value : (Depth, parent)
        d = {x: [None, None], y: [None, None]}

        def dfs(root, depth, parent):
            if root:
                if root.val == x or root.val == y:
                    d[root.val][0] = depth
                    d[root.val][1] = parent
                dfs(root.left, depth + 1, root)
                dfs(root.right, depth + 1, root)

        dfs(root, 0, None)

        if (d[x][0] == d[y][0]) and (d[x][1] is not d[y][1]):
            return True
        return False