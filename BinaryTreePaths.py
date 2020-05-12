# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import TreeNode

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        leftPathToLeaf = self.binaryTreePaths(root.left)
        rightPathToLeaf = self.binaryTreePaths(root.right)

        left = [str(root.val) + ("->" + lpath) for lpath in leftPathToLeaf]
        right = [str(root.val) + ("->" + rpath) for rpath in rightPathToLeaf]
        return left + right



if __name__ == "__main__":
    s = Solution()

    grandchild = TreeNode.TreeNode(5)
    lchild = TreeNode.TreeNode(2, None, grandchild)
    rchild = TreeNode.TreeNode(3)
    root = TreeNode.TreeNode(1, lchild, rchild)

    s.binaryTreePaths(root)