# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # p.left = parent.right
    # parent.right = p.right
    # p.right = parent
    # parent = p.left
    # p = left
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 自顶向下翻转：原左节点成为新根，原右节点成为新左，原根成为新右
        node, parent, parentRight = root, None, None
        while node is not None:
            left = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = left
        return parent