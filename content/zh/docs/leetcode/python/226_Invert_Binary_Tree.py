# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # 递归解法
    #     if root is None:
    #         return None
    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)
    #     root.left = right
    #     root.right = left
    #     return root

    def invertTree(self, root):
        # 迭代解法
        if root is None:
            return None
        queue = [root]
        while len(queue):
            curr = queue.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return root