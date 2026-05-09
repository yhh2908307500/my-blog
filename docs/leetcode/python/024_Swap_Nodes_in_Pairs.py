# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
class Solution(object):
    # def swapPairs(self, head):
    #     current = last = last2 = head
    #     while current is not None:
    #         nex = current.next
    #         if current == last.next:
    #             last.next = nex
    #             current.next = last
    #             if last == head:
    #                 head = current
    #             else:
    #                 last2.next = current
    #             last2 = last
    #             last = nex
    #         current = nex
    #     return head

    def swapPairs(self, head):
        # 虚拟头节点
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev, p = dummyHead, head
        # 两两交换节点
        while p != None and p.next != None:
            q, r = p.next, p.next.next
            # 交换p和q
            prev.next = q
            q.next = p
            p.next = r
            # 移动指针
            prev = p
            p = r
        return dummyHead.next
        