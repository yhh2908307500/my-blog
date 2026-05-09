# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def minDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # Recursion
    #     if root is None:
    #         return 0
    #     ld = self.minDepth(root.left)
    #     rd = self.minDepth(root.right)
    #     if ld != 0 and rd != 0:
    #         # handle 0 case!
    #         return 1 + min(ld, rd)
    #     return 1 + ld +rd

    def minDepth(self, root):
        # BFS：找到第一个叶子节点
        if root is None:
            return 0
        queue = [root]
        depth, rightMost = 1, root
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                break
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node == rightMost:
                # 到达当前层末尾
                depth += 1
                if node.right is not None:
                    rightMost = node.right
                else:
                    rightMost = node.left
        return depth

