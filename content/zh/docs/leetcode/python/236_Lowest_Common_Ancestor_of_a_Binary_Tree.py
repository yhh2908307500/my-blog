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
    #     self.ans = None

    #     def lowestCommonAncestorHelper(node):
    #         if not node:
    #             return False
    #         left = lowestCommonAncestorHelper(node.left)
    #         right = lowestCommonAncestorHelper(node.right)
    #         mid = node == p or node == q
    #         if mid + left + right >= 2:
    #             self.ans = node
    #         return mid or left or right
    #     lowestCommonAncestorHelper(root)
    #     return self.ans

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 使用栈遍历树
        stack = [root]
        # 字典存储父节点指针
        parent = {root: None}
        # 迭代直到找到p和q两个节点
        while p not in parent or q not in parent:

            node = stack.pop()

            # 遍历树时，保存父节点指针
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # p的祖先集合
        ancestors = set()

        # 使用父指针处理p的所有祖先
        while p:
            ancestors.add(p)
            p = parent[p]

        # q在p的祖先集合中出现的第一个祖先就是它们的最近公共祖先
        while q not in ancestors:
            q = parent[q]
        return q
