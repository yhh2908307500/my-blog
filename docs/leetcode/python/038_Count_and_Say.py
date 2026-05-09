class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        x = '1'
        while n > 1:
            # 每一轮读取上一轮的结果
            x = self.count(x)
            n -= 1
        return x

    def count(self, x):
        # 统计连续相同数字的个数
        m = list(x)
        res = []
        m.append(None)
        i , j = 0 , 0
        while i < len(m) - 1:
            j += 1
            if m[j] != m[i]:
                # j - i是m[i]的个数
                res += [j - i, m[i]]
                i = j
        return ''.join(str(s) for s in res)