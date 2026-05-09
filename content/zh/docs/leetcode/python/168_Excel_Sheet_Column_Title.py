class Solution:
    def convertToTitle(self, n: int) -> str:
        # 26进制转换：需要注意减1，因为A对应1而不是0
        res = ""
        while n > 0:
            n -= 1
            res = chr(65 + n % 26) + res
            n //= 26
        return res
