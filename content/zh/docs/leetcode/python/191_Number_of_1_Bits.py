class Solution(object):
    # def hammingWeight(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     # 方法1：使用bin函数转为二进制字符串后统计'1'的个数
    #     s_n = bin(n)[2:]
    #     return s_n.count('1')

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法2：位运算技巧，每次清除最低位的1
        # https://leetcode.com/articles/number-1-bits/
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
