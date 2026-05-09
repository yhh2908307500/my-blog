# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        # 快指针先走k步
        while k and fast.next:
            fast = fast.next
            length += 1
            k -= 1

        if k != 0:
            # 计算实际需要旋转的步数
            k = (k + length - 1) % length # original k % length
            return self.rotateRight(head, k)
        else:
            # 快慢指针一起走，直到快指针到达末尾
            while fast.next:
                fast = fast.next
                slow = slow.next
            return self.rotate(head, fast, slow)

    def rotate(self, head, fast, slow):
        # 连接头尾并断开新头前的连接
        fast.next = head
        head = slow.next
        slow.next = None
        return head