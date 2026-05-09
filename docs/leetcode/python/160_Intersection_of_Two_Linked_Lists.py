# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # https://leetcode.com/articles/intersection-two-linked-lists/
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 双指针：a走到A的末尾后从B开始走，b走到B的末尾后从A开始走，最终会在交点相遇
        if not headA or not headB:
            return None
        a, b = headA, headB
        ans = None
        while a or b:
            if not a:
                a = headB
            if not b:
                b = headA
            if a == b and not ans:
                ans = a
            a, b = a.next, b.next
        return ans
