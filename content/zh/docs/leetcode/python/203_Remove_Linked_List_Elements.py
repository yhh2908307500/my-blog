# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 添加一个虚拟头节点，方便处理头节点被删除的情况
        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        while pos is not None:
            if pos.val == val:
                # 跳过当前节点
                last.next = pos.next
            else:
                # 保留当前节点
                last = pos
            pos = pos.next
        return prehead.next

