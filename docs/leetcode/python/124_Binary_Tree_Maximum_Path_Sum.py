# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.result = -2147483647

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归：返回当前节点向父节点延伸的最大路径和
        self.getNodeMaxValue(root)
        return self.result

    def getNodeMaxValue(self, node):
        if node is None:
            return 0
        lresult = self.getNodeMaxValue(node.left)
        rresult = self.getNodeMaxValue(node.right)
        self.result = max(lresult + rresult + node.val, self.result)
        ret = node.val + max(lresult, rresult)
        # 如果左右最大路径和都是负的，就直接返回0
        if ret > 0:
            return ret
        return 0
