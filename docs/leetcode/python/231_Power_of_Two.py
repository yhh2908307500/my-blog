class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2的幂的二进制表示中只有一个1
        if n < 0:
            return False
        bin_str = bin(n)
        return sum(map(lambda x: int(x), list(bin_str[2:]))) == 1