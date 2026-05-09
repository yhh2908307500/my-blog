# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     # 方法1：使用栈，交换首尾节点的值
    #     if head is None:
    #         return
    #     stack = []
    #     pos = start = head
    #     while pos is not None:
    #         stack.append(pos)
    #         pos = pos.next
    #     while len(stack) > 0:
    #         if len(stack) >= 2:
    #             stack[0].val, stack[-1].val = stack[-1].val, stack[0].val
    #             stack.pop(0)
    #             stack.pop()
    #         else:
    #             stack.pop()
    #     return head
    #
    # def reverseList(self, head):
    #     # 方法2：递归 + 栈
    #     if head is None:
    #         return head
    #     stack = []
    #     pos = head
    #     while pos is not None:
    #         stack.append(pos)
    #         pos = pos.next
    #     pre_head = ListNode(-1)
    #     self.do_reverse(stack, pre_head)
    #     return pre_head.next
    #
    # def do_reverse(self, stack, curr_head):
    #     if len(stack) == 0:
    #         curr_head.next = None
    #         return
    #     node = stack.pop()
    #     curr_head.next = node
    #     curr_head = node
    #     self.do_reverse(stack, curr_head)

    # def reverseList(self, head):
    #     # 方法3：简单迭代，无需额外空间
    #     prev, curr = None, head
    #     while curr is not None:
    #         next_temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next_temp
    #     return prev

    def reverseList(self, head):
        # 方法4：递归，无需额外空间
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
