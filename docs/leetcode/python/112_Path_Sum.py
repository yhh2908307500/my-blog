# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 递归检查路径和
        if root is None:
            return False
        sum = sum - root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        # 检查左子树
        left = self.hasPathSum(root.left, sum)
        # 检查右子树
        right = self.hasPathSum(root.right, sum)
        return (left or right)
