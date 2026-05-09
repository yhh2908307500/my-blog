# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 找到最后一个非9的位置加1，后面都置0
        dummy = ListNode(0)
        dummy.next = head
        place_stop, tail = dummy, dummy
        while tail.next is not None:
            tail = tail.next
            if tail.val != 9:
                place_stop = tail
        if tail.val != 9:
            tail.val += 1
        else:
            place_stop.val += 1
            place_stop = place_stop.next
            while place_stop is not None:
                place_stop.val = 0
                place_stop = place_stop.next
        if dummy.val == 0:
            return dummy.next
        return dummy
