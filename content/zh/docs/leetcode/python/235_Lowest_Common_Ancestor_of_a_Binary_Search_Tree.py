# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # 获取所有可能路径
    #     paths = {}
    #     self.get_path(paths, root)
    #     # 比较p和q的路径
    #     # 返回最后一个相同的节点
    #     p_path, q_path = paths[p][::-1], paths[q][::-1]
    #     ls = min(len(p_path), len(q_path))
    #     pos = 0
    #     last = root
    #     while pos < ls:
    #         if p_path[pos] != q_path[pos]:
    #             return last
    #         last = p_path[pos]
    #         pos += 1
    #     return last
    #
    #
    # def get_path(self, paths, node, curr=[]):
    #     # 获取所有可能路径
    #     if node is not None:
    #         paths[node] = [node] + curr
    #         if node.left is not None:
    #             self.get_path(paths, node.left, paths[node])
    #         if node.right is not None:
    #             self.get_path(paths, node.right, paths[node])

    def lowestCommonAncestor(self, root, p, q):
        # 利用二叉搜索树性质缩小搜索空间
        if p is None or q is None or root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
