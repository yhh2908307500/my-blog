class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 先检查是否是2的幂，且1在偶数位
        return num > 0 and num & (num-1) == 0 and len(bin(num)[3:]) % 2 == 0