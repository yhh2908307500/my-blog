class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 使用集合记录出现过的数字，防止循环
        # https://en.wikipedia.org/wiki/Happy_number
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            # 计算各位数字的平方和
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        return n == 1