# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针：相遇后，慢指针回到开头，然后一起走，相遇点就是环的起点
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

