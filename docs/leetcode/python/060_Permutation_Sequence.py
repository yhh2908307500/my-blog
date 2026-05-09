class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 将第一个数字相同的排列视为一个块
        # 目标在 (k-1)/(n-1)! 块中
        remain = range(1, n + 1)
        if k <= 1:
            return ''.join(str(t) for t in remain)
        total = 1
        for num in remain[:-1]:
            total *= num
        res = self.do_getPermutation(remain, total, n - 1, k - 1)
        return ''.join(str(t) for t in res)


    def do_getPermutation(self, remain, curr, n, k):
        if n == 0 or k <= 0 or curr == 0:
            return remain
        # 计算在哪个块中
        step = k / curr
        # 剩余的k值
        k %= curr
        curr /= n
        res = [remain[step]] + self.do_getPermutation(remain[:step] + remain[step + 1:], curr, n - 1, k)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(3, 2)
    # print s.getPermutation(2, 2)