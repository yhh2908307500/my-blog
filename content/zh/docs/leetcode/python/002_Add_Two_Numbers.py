# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     # 进位值
    #     last = 0
    #     head = prev = None
    #     while True:
    #         # 两个链表都遍历完且没有进位时结束
    #         if l2 is None and l1 is None and last == 0:
    #             break
    #         val = last
    #         if l2 is not None:
    #             val += l2.val
    #             l2 = l2.next
    #         if l1 is not None:
    #             val += l1.val
    #             l1 = l1.next
    #         # 处理进位
    #         if val >= 10:
    #             val = val % 10
    #             last = 1
    #         else:
    #             last = 0
    #         current = ListNode(val)
    #         if prev is None:
    #             head = current
    #         else:
    #             prev.next = current
    #         prev = current
    #     return head

    def addTwoNumbers(self, l1, l2):
        # 进位值
        carry = 0
        # 虚拟头节点
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            # 当前位的值是val取模10
            curr.next = ListNode(val % 10)
            curr = curr.next
            # 进位是val除以10
            carry = int(val / 10)
        # 最后还有进位的话，添加一个节点
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
