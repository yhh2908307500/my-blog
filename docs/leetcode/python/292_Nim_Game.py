class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Nim游戏：只要n不是4的倍数就能赢
        return n % 4 != 0